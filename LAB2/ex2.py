# 2. Deschideti un fisier pentru citire, care contine o lista de cumparaturi (o generati de sine statator). Calculati suma toatala de cheltuieli.

# indicam denumirea fisierului pentru cumparaturi si initializam suma (sum)
myFile = "cumparaturi.txt"
sum = 0

# deschidem fisierul nostru in modul de citire
with open(myFile, "r") as file:
    # salvam randurile in variabila randuri
    randuri = file.readlines()
    # calculam numarul de randuri 
    count = len(randuri)

    # deschidem un ciclu for care va citi cu ajutorul variabilei rand fiecare rand din randuri
    for rand in randuri:
        # la semnul - se face split, adica se imparte randul in 2 
        primaParte = rand.strip().split("-")

        # daca prima parte este == 2
        if len(primaParte) == 2:
            # se salveaza in pretulProdus prima parte din rand
            pretulProdus = primaParte[1].strip()
            # pretulNumar produs se initializeaza cu variabila de tip string goala
            pretulNumarProdus = ""
            # se face un ciclu for in care char citeste fiecare element din pretulProdus

            for char in pretulProdus:
                # daca char este cifra se intra in if daca nu se trece mai departe
                if char.isdigit():
                    # se adauga char care contine numarul nostru a pretului in variabila pretulNumarProdus
                    pretulNumarProdus += char
                    
            # daca pretul numar produs are ceva se intra in if, daca nu se trece mai departe
            if pretulNumarProdus:
                # num i se atribuie pretNumarProdus care se transforma in integer
                num = int(pretulNumarProdus)
                # se printeaza elementul curent in care se indica produsul si pretul
                print(f"Produs: {primaParte[0].strip()}, Pretul: {num}")
                # se face suma totala
                sum += num

# se printeaza suma totala dupa finisarea for-ului principal
print("Suma totala a produselor este: {0}".format(sum))
