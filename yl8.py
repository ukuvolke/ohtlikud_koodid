year=int(input("Enter a year: "))
if (year %4==0) and not ((year %100==0) and (year %400!=0)):
    print("That is a leap year")
else:
    print("That is not a leap year")