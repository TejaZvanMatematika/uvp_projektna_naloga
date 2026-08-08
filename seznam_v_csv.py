import csv
import os


def shrani_v_csv(sez, pot):
    '''Funkcija zapiše podatke iz seznama v csv datoteko'''
    with open(pot, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(
            ['ID', 'priimek_ime', 'letnica rojstva', 'država', 'elo'])

        for sahist in sez:
            writer.writerow(sahist)
