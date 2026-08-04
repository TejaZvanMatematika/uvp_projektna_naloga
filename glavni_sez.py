import ast
import os

import mape_in_spletna_stran


def seznam_podatkov(sez_url_in_imen_dat, html_mapa, csv_mapa):
    '''Funkcija ki iz seznama, html mape, csv mape ustvari nov seznam
    s url linkom, html potjo, csv potjo in imenom spletne strani'''
    sez = []
    for url, ime in sez_url_in_imen_dat:
        html_pot = os.path.join(html_mapa, ime + '_koda.html')
        csv_pot = os.path.join(csv_mapa, ime + '_podatki.csv')
        ime_strani = mape_in_spletna_stran.pridobi_ime_strani(html_pot)

        sez.append((url, html_pot, csv_pot, ime_strani))

    return sez


def shrani_sez_v_dat(sez, pot):
    '''Funkcija ki shrani seznam v datoteko'''
    with open(pot, 'w', encoding='utf-8', newline='') as f:
        for tupl in sez:
            f.write(str(tupl) + '\n')


def shrani_dat_v_sez(pot):
    '''Funkcija ki hrani podatke datoteke v seznam'''
    sez = []

    with open(pot, 'r', encoding='utf-8') as f:
        for vrstica in f:
            vrstica = vrstica.strip()
            if vrstica != '':
                tupl = ast.literal_eval(vrstica)
                sez.append(tupl)
    return sez
