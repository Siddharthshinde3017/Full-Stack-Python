from flask import *
app = Flask(__name__)

@app.route("/")
def home():
    return "home"

@app.route("/route_test1")
def route_test1():
    name = "ABC"
    return render_template("test1.html", studentname = name)

@app.route("/route_test2")
def route_test2():
    num = 12
    return render_template("test2.html",num = num)

@app.route("/route_test3")
def route_test3():
    list1 = ["sid",33,22]
    return render_template("test3.html",mylist = list1)

@app.route("/route_test4")
def route_test4():
    dictionary = {1:"sid",
                  2:"yz"}
    return render_template("test4.html",mydict = dictionary)

if __name__ == "__main__" :
    app.run(debug=True)
