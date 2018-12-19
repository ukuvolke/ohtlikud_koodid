from random import randint
print("Ma mõtlen õhte numbrit, millist numbrit ma mõtlen? Arva ära!")
x=randint(1,100)
arvamine=int(input("Arva!"))
while arvamine !=x:
    if arvamine > x:
        print("Paku väiksem arv")
    else:
        print("Paku suurem arv")
    print ("Arva veel")
    arvamine=int(input("Arva!"))
print("Õigeeeeee!!!")