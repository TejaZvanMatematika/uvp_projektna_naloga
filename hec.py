import os


def stevnik(mapa):
    '''Funkcija, ki šteje kolikokrat se je program zagnal'''
    datoteka = 'stetje.text'
    pot = os.path.join(mapa, datoteka)
    stevilo = 1

    if os.path.exists(pot):
        with open(pot, 'r', encoding='utf-8') as f:
            st = f.read().strip()

        if st.isdigit():
            stevilo = int(st) + 1
        else:
            stevilo += 1
    else:
        stevilo = 1

    with open(pot, 'w', encoding='utf-8') as f:
        f.write(str(stevilo))

    return stevilo


def ponastavi(mapa):
    '''Funkcija ki resetira štetje'''
    datoteka = 'stetje.text'
    pot = os.path.join(mapa, datoteka)

    with open(pot, 'w', encoding='utf-8') as f:
        f.write('1')


def zahtevaj_opravicilo(mapa):
    '''Funkcija ki zahteva opravičilo od uporabnika, dokler ne dobi pravega
    vnosa je uporabnik zataknjen v loopu'''
    while True:
        opravicilo = input("Zahtevam opravičilo (napiši 'opravičujem se'):")
        if opravicilo.strip().lower() == 'opravičujem se':
            ponastavi(mapa)
            print('Opravičilo sprejeto, ponovno zaženi program. :)')
            break
        else:
            print('Ne, zahtevam opravičilo od tebe!')


def izbrisi_vse(sez, html_mapa, csv_mapa):
    '''Funkcija ki izbriše vse datoteke in mape'''
    for _, pot_html, pot_csv, _ in sez:
        os.remove(pot_html)
        os.remove(pot_csv)

    os.rmdir(html_mapa)
    os.rmdir(csv_mapa)
