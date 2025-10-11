

def display(abc):
    def inner1():
        print("function got changed")
    abc()
    return inner1
# @display
def show():
    print("This is show function")
show()

@display
def show2():
    print("show 2")
show2()

# @display
def show3():
    print("show3")
show3()