import csv
import os


def shrani_v_csv(sez, pot):
    '''Funkcija zapiše podatke iz seznama v csv datoteko'''
    with open(pot, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(
            ['ID', 'Priimek ime', 'Letnica rojstva', 'Država', 'Elo'])

        for sahist in sez:
            writer.writerow(sahist)
