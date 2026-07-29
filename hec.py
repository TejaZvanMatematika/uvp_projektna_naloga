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