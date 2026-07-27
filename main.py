import os

import mape_in_kode
import seznam_v_csv
import seznam


mape_in_kode.ustvari_csv_mapo('CSV_datoteke')


# Top 100 Players July 2026
URL_PLAYERS = 'https://ratings.fide.com/a_top.php?list=open'
MAPA_HTML_KODE = 'HTML_kode'
MAPA_CSV_DATOTEKE = 'CSV_datoteke'
POT_HTML_KODA_PLAYERS = os.path.join(MAPA_HTML_KODE, '100_players_koda.html')


mape_in_kode.shrani_spletno_stran_po_potrebi(URL_PLAYERS,
                                             MAPA_HTML_KODE,
                                             '100_players_koda.html')

with open(POT_HTML_KODA_PLAYERS, 'r', encoding='utf-8') as f:
    html_koda = f.read()

SEZ_PLAYER = seznam.seznam_podatkov(html_koda)

seznam_v_csv.shrani_v_csv(SEZ_PLAYER, MAPA_CSV_DATOTEKE, '100_players_podatki.csv')