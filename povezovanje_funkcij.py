import os

import mape_in_spletna_stran
import pregled
import seznam
import seznam_v_csv


def poveži(sez, html_mapa, csv_mapa):
    '''Funkcija logično poveže ostale funkcije'''
    pot_html = os.path.join(html_mapa, sez[1])
    pot_csv = os.path.join(csv_mapa, sez[2])

    mape_in_spletna_stran.shrani_spletno_stran(sez[0], pot_html)
    with open(pot_html, 'r', encoding='utf-8') as f:
        html_koda = f.read()

    sez_podatki = seznam.seznam_podatkov(html_koda)
    seznam_v_csv.shrani_v_csv(sez_podatki, pot_csv)
