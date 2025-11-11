from flask import *
app = Flask(__name__)           #to run the current file we use name

@app.route('/')

def home() :
    return "<h2>Hellow Flask<h2>"

@app.route('/about')

def about():
    return "About page"

@app.route("/contact")
def contact():
    return "Contact me on "

@app.route("/login")
def login():
    return "login "


if __name__ =="__main__":
    app.run(debug=True)