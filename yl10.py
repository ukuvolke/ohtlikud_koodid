nimekiri=["banaan", "apelsin", "õun"]
print(nimekiri[0])
nimekiri.append("kiivi")
print(nimekiri)
print (nimekiri[-1])
nimekiri[1]="tomat"
print(nimekiri)
if "kiivi" in nimekiri:
    print("kiivi on nimekirjas")
print(len(nimekiri))
nimekiri.remove("õun")
print(nimekiri)
nimekiri.reverse()
print(nimekiri)
nimekiri.sort()
print(nimekiri)