import random

print("Hey user choose option")

print("Choose 1 to generate password ")
print("Choose 2 to check strength of password ")

a = int(input("Enter no : "))
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
s = "!@#$%^&*()_-=+"

if(a == 1):
    password = random.randint(000000,999999)
    result = ""
    for i in range(6):
        result += random.choice(characters)
    password = str(password)
    special = random.choice(s)
    p = result+password+special

    print("Your password is ", p)

elif(a == 2):
    b = input("Enter your password : ")
    strength = len(b)
    if(strength<=4):
        print("Your password is weak" , b)

    elif(strength<=6):
        print("Your password is moderate")

    elif(strength<=8):
        print("Your password is strong")

    elif(strength>8):
        print("Your password is too strong" , b)

else:
    print("You choose wrong input , pls check it out")