#generator is function
# used to create iterators
# from fontTools.misc.cython import returns


def get_fun():
    for i in range(1,11):
        yield i
for i in get_fun():
    print(i)

def new_Str():
    a = "siddharth"
    yield a
    b= "Deepak"
    yield b
    c= "shinde"
    # return a+" "+b+" "+c
    yield c
n = new_Str()
print(next(n))
print(next(n))
print(next(n))
