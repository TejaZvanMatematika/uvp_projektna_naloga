import os
import requests

def shrani_spletno_stran_po_potrebi(url, ime_html_datoteke, mapa):
    '''Funkcija, ki sprejme url, ime html datoteke in ime mape,
    ta preveri če mapa že obstaja (če ne jo ustvari), potem pa
    preveri če obstaja pot do datoteke (če obstaja ne naredi nič,
    če ne pa pridobi html kodo iz url in shrani v html datoteko)
    '''
    pot = os.path.join(mapa, ime_html_datoteke)

    os.makedirs(mapa, exist_ok=True)

    if os.path.exists(pot):
        pass
    else:
        html_koda = requests.get(url).text
        with open(pot, 'w', encoding='utf-8') as f:
            f.write(html_koda)


def ustvari_csv_po_potrebi(mapa, ime_csv):
    '''Funkcija, ki pogleda za obstoj mape (če mape ni jo ustvari),
    in pogleda če je v mapi datoteka csv (če csv datoteke ni jo ustvari)
    '''
    pot = os.path.join(mapa, ime_csv)

    os.makedirs(mapa, exist_ok=True)

    if os.path.exists(pot):
        pass
    else:
        with open(pot, 'w', encoding='utf-8') as f:
            pass