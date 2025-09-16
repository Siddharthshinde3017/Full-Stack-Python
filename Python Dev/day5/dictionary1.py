my_dict = {1:"name"}
print(my_dict)

car = {1:"BMW", 2:"Mazda", 3: "Toyota"}
print(car)
print(type(car))

# accessing the values in the dictionary
print(car[2]+" is the 2nd company")

print(car.keys())
print(car.values())

# get()
cars = car.get(1)
print(cars)

# copy()
new_dict = car.copy()
print(new_dict)

# sorted()
print(sorted(car.keys()))
print(sorted(car.values()))
print(sorted(car.items()))

# pop()
# 1 specific item
car.pop(3)
print(car)

# 2 item at last
car.popitem()
print(car)

# update()
car.update({4:"suzuki"})
print(car)