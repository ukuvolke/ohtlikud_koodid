year=int(input("Sisesta aasta: "))
if (year %4==0) and not ((year %100==0) and (year %400!=0)):
    print("See on liigaasta.")
else:
    print("See ei ole liigaasta.")