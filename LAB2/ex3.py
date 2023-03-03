# 3. Deschideti un fisier pentru citire, care contine o lista de cumparaturi (o generati de sine statator). Calculati suma cheltuielilor pentru ultimele 3 zile.

import datetime

# deschidem fisierul de cumparaturi pentru citire
with open("cumparaturi2.txt", "r") as file:

    # calculam data de acum 3 zile
    today = datetime.date.today()
    three_days_ago = today - datetime.timedelta(days=3)

    # initializam variabila suma
    suma_cheltuieli = 0

    # citim fiecare linie din fisier
    for line in file:
        # impartim linia in cuvinte separate prin spatiu
        words = line.strip().split()

        # extragem prețul din ultimul cuvant
        pret_str = words[-1]
        pret = float(pret_str)

        # extragem data din prima parte a liniei, sub forma de string
        data_str = words[0]

        # convertim string-ul de data intr-un obiect datetime
        data = datetime.datetime.strptime(data_str, "%d.%m.%Y").date()

        # verificam daca data se incadreaza in ultimele 3 zile
        if data >= three_days_ago and data <= today:
            suma_cheltuieli += pret

    # afisam suma cheltuielilor pentru ultimele 3 zile
    print(f"Suma cheltuielilor pentru ultimele 3 zile este: {suma_cheltuieli:.2f} lei")
