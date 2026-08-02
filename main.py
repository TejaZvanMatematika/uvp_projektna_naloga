import sys

import mape_in_spletna_stran
import pregled
import hec
import povezovanje_funkcij


SEZ = [
    ('https://ratings.fide.com/a_top.php?list=open', '100_men_koda.html',
     '100_men_podatki.csv', 'Top 100 Players July 2026'),
    ('https://ratings.fide.com/a_top.php?list=women', '100_wemen_koda.html',
     '100_wemen_podatki.csv', 'Top 100 Women July 2026'),
    ('https://ratings.fide.com/a_top.php?list=men_rapid', '100_men_rapid_koda.html',
     '100_men_rapid_podatki.csv', 'Rapid Top 100 Players July 2026'),
    ('https://ratings.fide.com/a_top.php?list=women_rapid', '100_wemen_rapid_koda.html',
     '100_wemen_rapid_podatki.csv', 'Rapid Top 100 Women July 2026'),
    ('https://ratings.fide.com/a_top.php?list=men_blitz', '100_men_blitz_koda.html',
     '100_men_blitz_podatki.csv', 'Blitz Top 100 Players July 2026'),
    ('https://ratings.fide.com/a_top.php?list=women_blitz', '100_wemen_blitz_koda.html',
     '100_wemen_blitz_podatki.csv', 'Blitz Top 100 Women July 2026')
]
MAPA_HTML_KODE = 'HTML_kode'
MAPA_CSV_DATOTEKE = 'CSV_datoteke'

mape_in_spletna_stran.ustvari_mapo(MAPA_HTML_KODE)
mape_in_spletna_stran.ustvari_mapo(MAPA_CSV_DATOTEKE)


def main():
    spletne_strani_delujejo = True
    if pregled.brez_datotek(MAPA_CSV_DATOTEKE):
        for podsez in SEZ:
            if not pregled.preveri_nalaganje_spletne_strani(podsez[0]):
                print(f'Prišlo je do napake pri odpiranju spletne strani z'
                      f'naslovom {podsez[3]}. Poskusi znova.')
                spletne_strani_delujejo = False

    if not spletne_strani_delujejo:
        sys.exit()

    if pregled.brez_datotek(MAPA_CSV_DATOTEKE):
        for podsez in SEZ:
            povezovanje_funkcij.poveži(
                podsez, MAPA_HTML_KODE, MAPA_CSV_DATOTEKE)
        print('Nameščanje datotek končano.')
        hec.ponastavi()
    else:
        if pregled.preveri_vse_podatke(SEZ, MAPA_HTML_KODE, MAPA_CSV_DATOTEKE):
            st_poskusov = hec.stevnik()
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
                print(
                    f'Uspelo ti je priti do {st_poskusov}, sedaj te imam dovolj.')
            else:
                print('>:(')
                hec.izbrisi_vse(SEZ, MAPA_HTML_KODE, MAPA_CSV_DATOTEKE)
                hec.zahtevaj_opravicilo()
        else:
            for podsez in SEZ:
                if not pregled.preveri_podatke(podsez, MAPA_HTML_KODE, MAPA_CSV_DATOTEKE):
                    povezovanje_funkcij.poveži(
                        podsez, MAPA_HTML_KODE, MAPA_CSV_DATOTEKE)
                    print(
                        f'Ponovno naloženi podatki iz spletne strani {podsez[3]}.')
            print('Nameščanje datotek končano.')
            hec.ponastavi()


if __name__ == '__main__':
    main()
