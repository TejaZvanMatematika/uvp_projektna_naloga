import os
import requests
import re


def shrani_spletno_stran(url, pot):
    '''Funkcija, ki sprejme url in pot do datoteke,če pot ne obstaja
    shrani datoteko s spletno stranjotja, drugače ne naredi nič
    '''
    if os.path.exists(pot):
        pass
    else:
        html_koda = requests.get(url).text
        with open(pot, 'w', encoding='utf-8') as f:
            f.write(html_koda)


def ustvari_mapo(mapa):
    '''Funkcija, ki pogleda za obstoj mape (če mape ni jo ustvari)'''
    os.makedirs(mapa, exist_ok=True)


def pridobi_ime_strani(pot):
    '''Funkcija, ki pridobi naslov spletne strani iz kode'''
    with open(pot, 'r', encoding='utf-8') as f:
        koda = f.read()
    vzorec = r'<div class="title-page[^>]*>\s*(.*?)\s*</div>'
    return re.findall(vzorec, koda, flags=re.DOTALL)[0].strip()
