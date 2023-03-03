# 1. Deschideti un fisier pentru citire, afisati continutul pe ecran

# deschidem fisierul testFile.txt in modul de citire
myFile = open("testFile.txt", "r")

# printam continutul pe ecranul consolei
print(myFile.read())

# for x in myFile:
#     print(x)

# se inchide citirea fisierului
myFile.close()