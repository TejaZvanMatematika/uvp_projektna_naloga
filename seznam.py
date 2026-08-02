import re


def seznam_podatkov(html_koda):
    '''Funkcija sprejme html kodo, iz nje izlušči podatke o šahistih,
    potem pa te podatke shtrani v seznam na kar ta seznam shrani v seznam
    '''
    sez_vseh_podatkov = []

    vzorci = re.compile(
        r'<a href=/profile/(?P<ID>\d+)>(?P<priimek_ime>[^<]+)</a>.*?'
        r'<img[^>]+>\s*(?P<drzava>[A-Z]{3}).*?'
        r'<td>\s*(?P<elo>\d+)\s*</td>.*?'
        r'<td>\s*(?P<leto_rojstva>\d+)\s*</td>',
        flags=re.DOTALL
    )

    for vzorec in vzorci.finditer(html_koda):
        if len(sez_vseh_podatkov) < 100:
            Id = int(vzorec.group('ID'))
            priimek_ime = vzorec.group('priimek_ime').strip()
            drzava = vzorec.group('drzava')
            elo = int(vzorec.group('elo'))
            letnica_rojstva = int(vzorec.group('leto_rojstva'))

            priimek_ime = priimek_ime.replace(',', '')

            sez_vseh_podatkov.append(
                [Id, priimek_ime, letnica_rojstva, drzava, elo])

    return sez_vseh_podatkov
