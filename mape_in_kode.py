import os
import requests


def shrani_spletno_stran_po_potrebi(url, pot):
    '''Funkcija, ki sprejme url in pot do tja kamor želimo shraniti
    datoteko, če pot ne obstaja shrani datoteko s spletno stranjo
    tja, drugače ne naredi nič
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