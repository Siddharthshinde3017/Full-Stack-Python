import os.path
import sqlite3
import uuid

import bcrypt
from flask import *
from functools import wraps

from database_config import get_db
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "qwertyuiop"
app.config["UPLOAD_FOLDER"]= "D:\\Fortune Cloud\\Python Dev\\practice flask\\new_flask pro\\static\\uploads"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/admin/login", methods=["GET","POST"])
def admin_login():
    if  request.method == "POST":
        username = request.form["username"]
        password = request.form["password"].encode("utf-8")

        db=get_db()
        admin = db.execute("select * from admin where username = ?",(username,)).fetchone()
        if admin :
            stored_hash = admin["password_hash"]

            # Convert SQLite memoryview/blob → bytes
            if isinstance(stored_hash, memoryview):
                stored_hash = stored_hash.tobytes()
            elif isinstance(stored_hash, str):
                stored_hash = stored_hash.encode("utf-8")

            if bcrypt.checkpw(password,stored_hash):
                session["admin_id"]= admin["admin_id"]
                return redirect(url_for("admin_dashboard"))
        flash("Invalid Username or Password","danger")

    return render_template("admin_login.html")

def admin_required(f):
    @wraps(f)
    def wrapper(*args,**kwargs):
        if "admin_id" not in session:
            return redirect(url_for("admin_login"))
        return f(*args,**kwargs)
    return wrapper
@app.route("/admin/logout")
def admin_logout():
    session.pop("admin_id",None)
    return redirect(url_for("admin_login"))

@app.route("/admin/dashboard")
@admin_required
def admin_dashboard():
    db = get_db()

    total_properties = db.execute("SELECT COUNT(*) AS total FROM  properties").fetchone()["total"]

    total_buyers = db.execute("select count(*) AS total from buyers").fetchone()["total"]

    total_inquiries = db.execute("select count(*) AS total from inquiries").fetchone()["total"]

    return render_template("admin_dashboard.html",
                           total_properties=total_properties,
                           total_buyers = total_buyers,
                           total_inquiries = total_inquiries
                           )

@app.route("/admin/properties")
@admin_required
def admin_properties():
    db = get_db()
    properties = db.execute("""
    select p.*,(select image_url from property_images where property_id = p.property_id limit 1) AS image_url from properties p ORDER BY created_at DESC""").fetchall()

    return render_template("admin_properties.html",properties=properties)

@app.route("/properties")
def properties():
    db = get_db()
    properties = db.execute("select * from properties order by created_at DESC").fetchall()
    return  render_template("property_listing.html", properties = properties)


@app.route("/admin/properties/add-page")
@admin_required
def add_property_page():
    return render_template("admin_add_property.html")

@app.route("/admin/properties/add",methods=["POST"])
@admin_required
def add_property():
    db=get_db()

    data = (
        request.form["title"],
        request.form["type"],
        request.form["price"],
        request.form["location"],
        request.form["bedroom"],
        request.form["bathrooms"],
        request.form["area"],
        request.form["description"]

    )
    # con  = sqlite3.connect("real_estate.db")
    # cursor = con.cursor()
    cursor = db.cursor()
    cursor.execute(""" insert into properties (title, type, price, location, bedroom, bathrooms, area, description) 
     values(?,?,?,?,?,?,?,?)""",data)

    property_id = cursor.lastrowid

    #save images
    images = request.files.getlist("images")
    upload_folder = app.config["UPLOAD_FOLDER"]
    os.makedirs(upload_folder,exist_ok=True)

    for image in images:
        filename = secure_filename(image.filename)
        if filename =="":
            continue
        #gives unique name
        extension = filename.rsplit(".",1)[-1]
        filename = f"{uuid.uuid4().hex}.{extension}"

        image_path = os.path.join(upload_folder,filename)
        image.save(image_path)
        image_url = f"/static/uploads/{filename}"

        db.execute("""
        insert into property_images (property_id,image_url)
        values(?,?)""",(property_id,image_url))

    db.commit()
    flash("property added successfully")
    return redirect(url_for("admin_properties"))


@app.route("/admin/properties/delete/<property_id>")
@admin_required
def delete_property(property_id):
    db= get_db()

    #delete property images from db
    images = db.execute("select image_url from property_images where property_id = ?",(property_id,)).fetchall()

    #delete physical files from uploads folder
    for img in images:
        file_path = img["image_url"].replace("/static/uploads/","")
        full_path = os.path.join(app.config["UPLOAD_FOLDER"],file_path)
        if os.path.exists(full_path):
            os.remove(full_path)

    #delete image record from property_images
    db.execute("delete from property_images where property_id = ?",(property_id,))

    #delete propertty itself
    db.execute("delete from properties where property_id = ?",(property_id,))

    db.commit()
    flash("Property deleted successfully")
    return redirect(url_for("admin_properties"))

@app.route("/admin/properties/edit/<int:property_id>")
@admin_required
def edit_property_page(property_id):
    db = get_db()
    property_data = db.execute("select * from properties where property_id = ?",(property_id,)).fetchone()
    images = db.execute("select * from property_images where property_id = ?",(property_id,)).fetchall()

    if not property_data:
        flash("property not found","danger")
        return redirect(url_for("admin_properties"))
    return render_template("edit_property.html",property=property_data,images=images)

@app.route("/admin/properties/update/<int:property_id>",methods = ["POST"] )
@admin_required
def update_property(property_id):
    db = get_db()

    data = (
        request.form["title"],
        request.form["type"],
        request.form["price"],
        request.form["location"],
        request.form["bedroom"],
        request.form["bathrooms"],
        request.form["area"],
        request.form["description"],
        property_id
    )
    db.execute("""
    update properties set title = ?,type = ?,price = ?,location= ?,bedroom = ?,bathrooms = ?,area = ?,description = ? where property_id = ?
    """,data)
    # handle new uploaded images (optional)
    images = request.files.getlist("images")
    upload_folder = app.config["UPLOAD_FOLDER"]

    for image in images:
        filename = secure_filename(image.filename)
        if filename == "":
            continue

        extension = filename.rsplit(".",1)[-1]
        filename = f"{uuid.uuid4().hex}.{extension}"
        image_path = os.path.join(upload_folder,filename)
        image.save(image_path)

        image_url = f"/static/uploads/{filename}"
        db.execute("insert into property_images(property_id,image_url) values(?,?)",(property_id,image_url))
    db.commit()
    flash("Property updated successfully","success")
    return redirect(url_for("admin_properties"))

@app.route("/admin/properties/delete-image/<int:image_id>")
@admin_required
def delete_property_image(image_id):
    db = get_db()

    #get image info first
    image = db.execute("select * from property_images where image_id = ?",(image_id,)).fetchone()
    if not image:
        flash("Image not found","danger")
        return redirect(url_for("admin_properties"))

    #delete actual file
    file_path = image["image_url"].replace("/static/uploads/","")
    full_path = os.path.join(app.config["UPLOAD_FOLDER"],file_path)
    if os.path.exists(full_path):
        os.remove(full_path)

    #delete from db
    property_id = image["property_id"]
    db.execute("Delete from property_images where image_id = ?",(image_id,))
    db.commit()

    flash("Image deleted successfully","success")
    return redirect(url_for("edit_property_page",property_id = property_id))


@app.route("/admin/inquiries")
@admin_required
def admin_inquiries():
    db = get_db()
    inquiries = db.execute("""
    select i.*,p.title AS property_title
    from inquiries i 
    left join properties p ON p.property_id = i.property_id
    order by i.created_at desc
    """).fetchall()
    return render_template("admin_inquiries.html",inquiries =inquiries)

@app.route("/admin/inquiries/respond/<int:inquiry_id>")
@admin_required
def respond_inquiry(inquiry_id):
    db = get_db()
    db.execute("update inquiries set status = 'Responded' where inquiry_id =? ",(inquiry_id,))
    db.commit()

    flash("Inquiry marked as responded", "success")
    return redirect(url_for('admin_inquiries'))




if __name__=="__main__":
    app.run(debug=True,port=1234)