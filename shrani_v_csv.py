import csv


def shrani_v_csv(sez, ime_csv):
    '''Funkcija zapiše podatke iz seznama v csv datoteko'''
    with open(ime_csv, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['ID', 'Priimek ime', 'Letnica rojstva', 'Država', 'Elo'])

        for sahist in sez:
            writer.writerow(sahist)