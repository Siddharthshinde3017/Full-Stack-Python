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
    return render_template("admin_dashboard.html")

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


@app.route("/admin/properties/add",methods=["POST"])
@admin_required
def add_property():
    db=get_db()

    data = (
        request.form["title"],
        request.form["type"],
        request.form["price"],
        request.form["location"],
        request.form["bedrooms"],
        request.form["bathrooms"],
        request.form["area"],
        request.form["description"]

    )
    # con  = sqlite3.connect("real_estate.db")
    # cursor = con.cursor()
    cursor = db.cursor()
    cursor.execute(""" insert into properties (title, type, price, location, bedrooms, bathrooms, area, description) 
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
    return redirect(url_for("properties"))

if __name__=="__main__":
    app.run(debug=True,port=1234)