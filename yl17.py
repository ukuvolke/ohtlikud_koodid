from random import randint
valikud=["kivi", "paber", "käärid"]
inime=False
while inime==False:
    comp=valikud[randint(0,2)]
    
    inime=input("Sisesta kivi, paber või käärid: ")
    if comp==inime:
        print("Viik!")
    elif inime == "kivi":
        if comp == "paber":
            print("Kaotasid!")
        else:
            print("Võitsid!")
    elif inime == "paber":
        if comp== "käärid":
            print("Kaotasid!")
        else:
            print("Võitsid!")
    elif inime =="käärid":
        if comp=="kivi":
            print("Kaotasid!")
        else:
            print("Võitsid!")
    else:
        print("Sellist käiku pole olemas!")
    end=input("Kas tahad veel mängida? (jah/ei) ")
    if end=="ei":
        exit()
    inime = False