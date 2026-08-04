import os

import mape_in_spletna_stran
import glavni_sez
import pregled
import seznam
import seznam_v_csv
import hec


SEZ_URL_IN_IMEN_DAT = [
    ('https://ratings.fide.com/a_top.php?list=open', '100_men'),
    ('https://ratings.fide.com/a_top.php?list=women', '100_wemen'),
    ('https://ratings.fide.com/a_top.php?list=men_rapid', '100_men_rapid'),
    ('https://ratings.fide.com/a_top.php?list=women_rapid', '100_wemen_rapid'),
    ('https://ratings.fide.com/a_top.php?list=men_blitz', '100_men_blitz'),
    ('https://ratings.fide.com/a_top.php?list=women_blitz', '100_wemen_blitz')
]
MAPA_HTML_KODE = 'HTML_kode'
MAPA_CSV_DATOTEKE = 'CSV_datoteke'
MAPA_POMOZNE_DATOTEKE = 'pomozne_datoteke'
SEZ = []


def main():
    mape_in_spletna_stran.ustvari_mapo(MAPA_HTML_KODE)
    mape_in_spletna_stran.ustvari_mapo(MAPA_CSV_DATOTEKE)
    mape_in_spletna_stran.ustvari_mapo(MAPA_POMOZNE_DATOTEKE)

    if pregled.brez_datotek(MAPA_HTML_KODE):
        pregled.preveri_dostopnost_spletnih_strani(SEZ_URL_IN_IMEN_DAT)
        for url, ime in SEZ_URL_IN_IMEN_DAT:
            html_pot = os.path.join(MAPA_HTML_KODE, ime + '_koda.html')
            mape_in_spletna_stran.shrani_spletno_stran(url, html_pot)
        print('HTML kode uspešno naložene.')

    pot_dat = os.path.join(MAPA_POMOZNE_DATOTEKE, 'sez.text')
    global SEZ
    if os.path.exists(pot_dat):
        SEZ = glavni_sez.shrani_dat_v_sez(pot_dat)
    else:
        SEZ = glavni_sez.seznam_podatkov(
            SEZ_URL_IN_IMEN_DAT, MAPA_HTML_KODE, MAPA_CSV_DATOTEKE)
        glavni_sez.shrani_sez_v_dat(SEZ, pot_dat)

    if pregled.brez_datotek(MAPA_CSV_DATOTEKE):
        for _, pot_html, pot_csv, _ in SEZ:
            with open(pot_html, 'r', encoding='utf-8') as f:
                koda = f.read()
            sez = seznam.sez_podatkov_za_csv(koda)
            seznam_v_csv.shrani_v_csv(sez, pot_csv)
        hec.ponastavi(MAPA_POMOZNE_DATOTEKE)
        print('CSV datoteke uspešno naložene.')
        print('Vse datoteke uspešno naložene.')
    else:
        if not pregled.preveri_vse_podatke(SEZ):
            for _, pot_html, pot_csv, ime in SEZ:
                if not pregled.preveri_podatke(pot_html, pot_csv):
                    with open(pot_html, 'r', encoding='utf-8') as f:
                        koda = f.read()
                    sez = seznam.sez_podatkov_za_csv(koda)
                    seznam_v_csv.shrani_v_csv(sez, pot_csv)
                    print(f'Ponovno naloženi podatki v CSV datoteko '
                          f'iz spletne strani {ime}.')
            print('CSV datoteke uspešno naložene.')
            hec.ponastavi(MAPA_POMOZNE_DATOTEKE)
        else:
            st_poskusov = hec.stevnik(MAPA_POMOZNE_DATOTEKE)
            if st_poskusov < 5:
                print('Datoteke so že nameščene.')
            elif st_poskusov == 5:
                print('Kolikokrat moraš še poskusiti?')
            elif st_poskusov == 6:
                print('Še vedno vstrajaš?')
            elif st_poskusov == 7:
                print('No prav, bom pa začel šteti tvoje poskuse.')
            elif st_poskusov < 100:
                print(f'To je {st_poskusov} poskus.')
            elif st_poskusov == 100:
                print(f'Uspelo ti je priti do {st_poskusov}-tega poskusa, '
                      'sedaj te imam dovolj.')
            else:
                print('Izbrisal sem ti vse >:(')
                hec.izbrisi_vse(SEZ, MAPA_HTML_KODE, MAPA_CSV_DATOTEKE)
                hec.zahtevaj_opravicilo(MAPA_POMOZNE_DATOTEKE)


if __name__ == '__main__':
    main()
