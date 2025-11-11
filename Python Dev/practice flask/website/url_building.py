from doctest import debug

from flask import *

app = Flask(__name__)

@app.route("/")
def home():
    return  "URL Building"

@app.route("/welcome/<name>")
def welcome(name):
    return "Welcome %s" %name

@app.route("/rollno/<int:num>")
def rollno(num):
    return "rollno is %d" %num


if __name__ == "__main__":
    app.run(debug= True)