import os

import mape_in_kode
import seznam_v_csv
import seznam


MAPA_HTML_KODE = 'HTML_kode'
MAPA_CSV_DATOTEKE = 'CSV_datoteke'

mape_in_kode.ustvari_mapo(MAPA_HTML_KODE)
mape_in_kode.ustvari_mapo(MAPA_CSV_DATOTEKE)


SEZ = [
    ('https://ratings.fide.com/a_top.php?list=open', '100_men_koda.html',
     '100_men_podatki.csv'),
    ('https://ratings.fide.com/a_top.php?list=women', '100_wemen_koda.html',
     '100_wemen_podatki.csv'),
    ('https://ratings.fide.com/a_top.php?list=men_rapid', '100_men_rapid_koda.html',
     '100_men_rapid_podatki.csv'),
    ('https://ratings.fide.com/a_top.php?list=women_rapid', '100_wemen_rapid_koda.html',
     '100_wemen_rapid_podatki.csv'),
    ('https://ratings.fide.com/a_top.php?list=men_blitz', '100_men_blitz_koda.html',
     '100_men_blitz_podatki.csv'),
    ('https://ratings.fide.com/a_top.php?list=women_blitz', '100_wemen_blitz_koda.html',
     '100_wemen_blitz_podatki.csv')
]


for sez in SEZ:
    pot_html = os.path.join(MAPA_HTML_KODE, sez[1])
    pot_csv = os.path.join(MAPA_CSV_DATOTEKE, sez[2])

    mape_in_kode.shrani_spletno_stran_po_potrebi(sez[0], pot_html)
    with open(pot_html, 'r', encoding='utf-8') as f:
        html_koda = f.read()

    sez_podatki = seznam.seznam_podatkov(html_koda)
    seznam_v_csv.shrani_v_csv(sez_podatki, pot_csv)
