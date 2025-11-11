from flask import *

app = Flask(__name__)

@app.route("/")
def home():
    return "select login of ....."

@app.route("/student_login")
def student_login():
    return render_template("student_login.html")

@app.route("/hr_login")
def hr_login():
    return render_template("hr_login.html")

@app.route("/login/<user>")
def login(user):
    if user == "student" :
        return redirect(url_for("student_login"))
    elif user == "hr":
        return  redirect(url_for("hr_login"))
    else:
        return "Invalid choice"

if __name__ == "__main__":
    app.run(debug=True)