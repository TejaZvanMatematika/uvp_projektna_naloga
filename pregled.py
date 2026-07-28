import os


def preveri_podatke(sez, html_mapa, csv_mapa):
    '''Funkcija ki sprejme seznam podatkov in imena map, pogleda ce
    mape obstajata in ce je v csv 101 vrstic
    '''
    for _, dat_html, dat_csv in sez:
        pot_html = os.path.join(html_mapa, dat_html)
        pot_csv = os.path.join(csv_mapa, dat_csv)

        if not os.path.exists(pot_html) or not os.path.exists(pot_csv):
            return False

        with open(pot_csv, 'r', encoding='utf-8') as f:
            csv = f.readlines()

        if len(csv) != 101:
            return False
        
    return True