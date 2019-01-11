def countA(text):
    count = 0
    for c in text:
        if c == ("a")or c== ("e")or c==("i")or c==("o")or c==("u")or c==("õ")or c==("ä")or c==("ö")or c==("ü"):
            count = count + 1
    return count
sisend=str(input("Sisesta tekst milles olevate täishäälikute arvu tahad teada: ").lower())
print(countA(sisend))