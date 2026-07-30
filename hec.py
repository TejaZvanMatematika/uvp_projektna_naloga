import os


def stevnik():
    '''Funkcija, ki šteje kolikokrat se je program zagnal'''
    datoteka = 'stetje.text'
    stevilo = 1

    if os.path.exists(datoteka):
        with open(datoteka, 'r', encoding='utf-8') as f:
            st = f.read().strip()

        if st.isdigit():
            stevilo = int(st) + 1
        else:
            stevilo += 1
    else:
        stevilo += 1

    with open(datoteka, 'w', encoding='utf-8') as f:
        f.write(str(stevilo))

    return stevilo


def ponastavi():
    '''Funkcija ki resetira štetje'''
    datoteka = 'stetje.text'

    with open(datoteka, 'w', encoding='utf-8') as f:
        f.write('1')


def zahtevaj_opravicilo():
    '''Funkcija ki zahteva opravičilo od uporabnika'''
    while True:
        opravicilo = input("Zahtevam opravičilo (napiši 'opravičujem se'):")
        if opravicilo.strip().lower() == 'opravičujem se':
            ponastavi()
            print('Opravičilo sprejeto, ponovno zaženi program :)')
            break
        else:
            print('Ne, zahtevam opravičilo od tebe')


def izbrisi_vse(sez, html_mapa, csv_mapa):
    '''Funkcija ki izbrise vse datoteke in mape'''
    for podsez in sez:
        pot_html = os.path.join(html_mapa, podsez[1])
        pot_csv = os.path.join(csv_mapa, podsez[2])

        os.remove(pot_html)
        os.remove(pot_csv)

    os.rmdir(html_mapa)
    os.rmdir(csv_mapa)
