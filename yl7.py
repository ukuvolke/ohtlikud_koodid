name=str(input("Tere, mis su nimi on?").capitalize())
home=str(input("Tere "+name+"! Kus sa elad? ").lower())
if (home=="saaremaa") or (home=="saaremaal"):
    print("Äge, mina ka!")
age=int(input("Kui vana sa oled?"))
if age<18:
    print(name+", Sa oled liiga noor, et autoga sõita!")
elif age==18:
    print("Palju õnne täiskasvanuks saamise puhul, "+name+"!" )
else:
    print("Sa võid autoga sõita!")
