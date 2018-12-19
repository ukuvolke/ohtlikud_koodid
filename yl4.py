a= int(input("Please enter digit no. 1: "))
b= int(input("Please enter digit no. 2: "))
c= int(input("Please enter digit no. 3: "))
if (a > b) and  ( a > c):
    print("Digit 1 is the largest.")
elif (b > a) and (b>c):
    print("Digit 2 is the largest.")
else:
    print("Digit 3 is the largest.")