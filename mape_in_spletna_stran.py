import os
import requests


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
