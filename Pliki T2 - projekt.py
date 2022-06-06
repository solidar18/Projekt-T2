pierwsza_linia = "10;EOLPXXXXXX;EOLP RETURN TO SUPPLIER;PLV;LENS_GD;;;;;;VENDOR_RTN_FI;;;;"
polecenie_opc = "20;XXXXXXXXXX;X;;;"
                
plik = input("Podaj nazwe pliku: ")

# ==================================
import datetime

teraz = datetime.datetime.now()
data = teraz.strftime("%d%m%y")

plik_wyjsciowy = f"SC{data}.txt"

# dzien = teraz.day
# miesiac = teraz.month
# rok = teraz.year

# # ===================================
# if dzien <= 9:
#     dzien_wynik = f"0{dzien}"
# else:
#     dzien_wynik = f"{dzien}"
# if miesiac <= 9:
#     miesiac_wynik = f"0{miesiac}"
# else:
#     miesiac_wynik = f"{miesiac}"
# rok_wynik = f"{rok % 100}" # reszta z dzielenia 
# data = f"{dzien_wynik}{miesiac_wynik}{rok_wynik}"
# ====================================

pierwsza_linia = pierwsza_linia.replace("XXXXXX" , data)

print(pierwsza_linia)

with open(plik) as dane, open(plik_wyjsciowy,"w") as plik:
    plik.write(pierwsza_linia)
    plik.write("\n")
    for line in dane:
        line = line.strip()
        lista = line.split(";")
        opc = lista[0]
        qty = lista[1]
        polecenie = polecenie_opc.replace("XXXXXXXXXX", opc)
        polecenie = polecenie.replace("X", qty)
        plik.write(polecenie)
        plik.write("\n")
        print(polecenie)
        