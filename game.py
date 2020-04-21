# Author: Diliano
# Comment: d.y.73@mail.ru
# A fun little python game
name = input("What's your name?")
age = int(input("What's your age?"))
age_years = age+100
likes_pizza = True

print("Hi, " + name + "!")
print("Your age is " + str(age) + " and in 100 years you are going to be in your " + str(age_years))

if(likes_pizza == True):
    print("Whoa!")