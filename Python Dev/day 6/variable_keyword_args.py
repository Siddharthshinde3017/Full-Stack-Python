from tkinter.font import names


def showinfo(**info):
    for k, v in info.items():
        print(k,v)
showinfo(name="sid",age=21)

def describe(**features):
    print(features)
describe(height=170,width= 60)

# capitalize names
def capitalized(**names):
    for k,v in names.items():
        print(v.upper())
capitalized(friend= "siddharth",)

