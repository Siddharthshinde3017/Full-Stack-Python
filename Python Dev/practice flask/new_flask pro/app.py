from flask import *

app = Flask(__name__)
app.secret_key = "qwertyuiop"
app.config["UPLOAD_FOLDER"]= "D:\\Fortune Cloud\\Python Dev\\practice flask\\new_flask pro\\static\\uploads"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/Admin_login")
def admin_login():
    return render_template("Admin_login.html")


@app.route("/admin_dashboard")
def admin_dashboard():
    return render_template("admin_dashboard.html")

if __name__=="__main__":
    app.run(debug=True,port=1234)