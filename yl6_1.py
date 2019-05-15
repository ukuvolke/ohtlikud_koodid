import math
pi=math.pi
print("Tere, olen programm mis arvutab sisestatud raadiuse põhjal ringi ümbermõõdu ja diameetri.")
r=int(input("Palun sisesta raadius: "))
perimeter=2*pi*r
area=(r*r)*pi
print("Sisestatud raadiusega ringi ümbermõõt on " + str(round(perimeter, 2)) + " ühikut ja pindala on " + str(round(area, 2))+ " ühikut.")