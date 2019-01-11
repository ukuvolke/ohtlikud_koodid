

upc=input("Enter the code plz: ").zfill(11)
print(upc)
sum1=int(upc[0])+int(upc[2])+int(upc[4])+int(upc[6])+int(upc[8])+int(upc[10])
sum2=int(upc[1])+int(upc[3])+int(upc[5])+int(upc[7])+int(upc[9])
sum3=int(sum1)*3
sum4=sum3+sum2
M=sum4%10
if M==0:
    print("Viimane arv on 0")
else:
    print("Viimane arv on",10-M)