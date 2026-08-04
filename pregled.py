import os
import requests


def preveri_vse_podatke(sez):
    '''Funkcija ki sprejme seznam podatkov in imena map, pogleda ce
    mape obstajata in ce je csv dolg 101 vrstic in ima 5 stolpcev
    '''
    for _, pot_html, pot_csv, _ in sez:
        if not os.path.exists(pot_html) or not os.path.exists(pot_csv):
            return False
        else:
            with open(pot_csv, 'r', encoding='utf-8') as f:
                csv = f.readlines()

        if len(csv) != 101:
            return False

        for vrstica in csv:
            stolpci = vrstica.strip().split(',')
            if len(stolpci) != 5:
                return False

    return True


def preveri_podatke(pot_html, pot_csv):
    '''Funkcija ki sprejme seznam podatkov in imena map, pogleda ce
    mape obstajata in ce je csv dolg 101 vrstic in ima 5 stolpcev
    '''
    if not os.path.exists(pot_html) or not os.path.exists(pot_csv):
        return False
    else:
        with open(pot_csv, 'r', encoding='utf-8') as f:
            csv = f.readlines()

    if len(csv) != 101:
        return False

    for vrstica in csv:
        stolpci = vrstica.strip().split(',')
        if len(stolpci) != 5:
            return False

    return True


def preveri_dostopnost_spletne_strani(url):
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


def preveri_dostopnost_spletnih_strani(sez_url_in_imena_dat):
    '''Funkcija preveri dostopnost vseh spletnih strani'''
    for url, _ in sez_url_in_imena_dat:
        if not preveri_dostopnost_spletne_strani(url):
            print('Prišlo je do napake pri nalaganju spletnih strani, poskusi še enkrat')
