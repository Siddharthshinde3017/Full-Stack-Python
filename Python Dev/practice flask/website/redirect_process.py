from flask import *
app = Flask(__name__)

@app.route("/")
def home():
    return redirect(url_for("about"))

@app.route("/home")
def about():
    return render_template("about.html")



if __name__ == "__main__":
    app.run(debug=True)