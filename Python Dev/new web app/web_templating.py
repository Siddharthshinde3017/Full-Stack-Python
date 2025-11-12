from flask import*
app = Flask(__name__)

@app.route("/")
def home():
    return "Home"

@app.route("/test1")
def test1():
    name = "ABC"
    return render_template("test1.html",studentname = name)

@app.route("/test2")
def test2():
    num = 12
    return render_template("test2.html",num = num)

@app.route("/test3")
def test3():
    list1 = [11,22,44]
    return render_template("test2.html",list1 = list1)


if __name__ == "_main_":
    app.run(debug=True,port=1911)