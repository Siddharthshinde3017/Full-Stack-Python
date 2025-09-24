# sum of numbers variable length args
def total(*numbers):
    print(sum(numbers))
total(1, 2, 3)
total(5, 10)

# list of pets
def show(*pets):
    for pet in pets:
        print(pet)
show("Dog", "Cat")

# minimum and maximum
def minmax(*values):
    print("minimum value is",min(values),"& maximum value is", max(values))
minmax(1, 2, 3, 4)

# string concat
def concat(*elements):
    print("".join(elements))
concat("a", "b", "c")
# argument counter
def count_args(*args):
    print(len(args))
count_args(1, 2, 3, 4)