name=str(input("Hello what is your name?").capitalize())
home=str(input("Hello "+name+"! Where do you live? ").lower())
if (home=="saaremaa") or (home=="saaremall"):
    print("Cool, me too!")
age=int(input("How old are you?"))
if age<18:
    print(name+", You are too young to drive a car!")
elif age==18:
    print("Congratulations for being an adult, "+name+"!" )
else:
    print("You can drive a car!")
