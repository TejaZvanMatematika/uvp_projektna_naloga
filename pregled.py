import os
import requests


def preveri_vse_podatke(sez, html_mapa, csv_mapa):
    '''Funkcija ki sprejme seznam podatkov in imena map, pogleda ce
    mape obstajata in ce je csv dolg 101 vrstic
    '''
    for _, dat_html, dat_csv, _ in sez:
        pot_html = os.path.join(html_mapa, dat_html)
        pot_csv = os.path.join(csv_mapa, dat_csv)

        if not os.path.exists(pot_html) or not os.path.exists(pot_csv):
            return False
        else:
            with open(pot_csv, 'r', encoding='utf-8') as f:
                csv = f.readlines()

        if len(csv) != 101:
            return False
                    
    return True


def preveri_podatke(sez, html_mapa, csv_mapa):
    '''Funkcija ki sprejme seznam podatkov in imena map, pogleda ce
    mape obstajata in ce je csv dolg 101 vrstic
    '''
    pot_html = os.path.join(html_mapa, sez[1])
    pot_csv = os.path.join(csv_mapa, sez[2])

    if not os.path.exists(pot_html) or not os.path.exists(pot_csv):
        return False
    else:
        with open(pot_csv, 'r', encoding='utf-8') as f:
            csv = f.readlines()

    if len(csv) != 101:
        return False
                
    return True


def preveri_nalaganje_spletne_strani(url):
    '''Funkcija ki preveri če pride do napake pri odpiranju spletne 
    strani
    '''
    glava = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    try:
        odgovor = requests.get(url, headers=glava, timeout=10)
        return odgovor.status_code == 200
    except requests.RequestException:
        return False


def brez_datotek(csv_mapa):
    '''Funkcija, ki preveri če mapa vsebuje datoteke (True če je prazna)
    '''
    if len(os.listdir(csv_mapa)) == 0:
        return True