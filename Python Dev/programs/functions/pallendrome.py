def is_pallendrome(str1):
    str_rev = str1[::-1]
    if str1 == str_rev:
        print("It is a Pallendrome")
    else:
        print("Not Pallendrome")
str1 = str(input("enter the string "))
is_pallendrome(str1)