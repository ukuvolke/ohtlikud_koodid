print("Tere, see on kolmnurga tüübi arvutamise masin.")
a=float(input("sisesta külje a pikkus: "))
b=float(input("sisesta külje b pikkus: "))
c=float(input("sisesta külje c pikkus: "))
if (a==b) and (b==c):
    print("Kolmnurk on võrdkülgne")
elif (((a+b)<c) or ((b+c)<a) or ((c+a)<b)):
    print("Sellist kolmurka pole olemas")
elif (a==b) or (b==c) or (c==a) and not (((a+b)<c) or ((b+c)<a) or ((c+a)<b)):
    print("Kolmnurk on võrdhaarne")
else:
    print("Kolmnurk on erikülgne ")