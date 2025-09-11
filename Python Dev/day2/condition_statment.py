# conditional statements

# if statement
# a= int(input("enter the number : "))
# # a=0
# if a%2 ==0:
#     print("number is even")
# else:
#     print("number is odd")
#
#

# elif
age = 15
if age == 15:
    print("you can apply for ssc")
elif age == 18:
    print("you can apply for hsc")
elif age == 20 :
    print("you can appy for degree ")
else :
    print("go and watch pogo")


# nested if
number = 20

if number%2 == 0 :
    print("even number")
    if number > 0:
        print("number is positive")
    if number<0:
        print("number is negative")
else :
    print("number is odd")


