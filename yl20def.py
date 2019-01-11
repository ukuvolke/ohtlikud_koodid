def kontrollsumma(kood):

    upc=str(kood).zfill(11)
    sum1=int(upc[0])+int(upc[2])+int(upc[4])+int(upc[6])+int(upc[8])+int(upc[10])
    sum2=int(upc[1])+int(upc[3])+int(upc[5])+int(upc[7])+int(upc[9])
    sum3=int(sum1)*3
    sum4=sum3+sum2
    M=sum4%10
    return M if M==0 else 10-M

print (kontrollsumma(3600029145))