# GEMINI


## pregled - funkcija preveri_nalaganje_spletne_strani
**Jaz:**
usmeri me kako lahko pogledam ce se lahko koda websita lahko nalozi dol ali ne v pythonu

**Gemini:**
Preverjanje dostopnosti in prenosa kode (HTTP Status)
Če želiš preizkusiti, ali strežnik dovoljuje prenos HTML kode strani, to storiš z knjižnico requests. S preverjanjem statusne kode (200 OK) vidiš, ali je stran javno dostopna in ali ti strežnik ne vrača napak (npr. 403 Forbidden ali 401 Unauthorized).

Python
import requests

def preveri_in_prenesi_kodo(url):
    try:
        # Uporabimo User-Agent, da simulišemo brskalnik (nekatere strani blokirajo gole skripte)
        glave = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        
        odgovor = requests.get(url, headers=glave, timeout=10)
        
        # Preverimo statusno kodo
        if odgovor.status_code == 200:
            print(f"Stran je dostopna! (Status: {odgovor.status_code})")
            print(f"Dolžina kode: {len(odgovor.text)} znakov.")
            return odgovor.text
        elif odgovor.status_code == 403:
            print("Dostop zavrnjen (403 Forbidden). Stran blokira samodejne prenose.")
        elif odgovor.status_code == 401:
            print("Potrebna je avtentikacija / prijava (401 Unauthorized).")
        else:
            print(f"Težava pri dostopu. Statusna koda: {odgovor.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"Napaka pri povezavi: {e}")
    
    return None


**Jaz**
kako naredim da se mi izpise nekaj po for zanki le ce je vse uspesno koncano

**Gemini**
Uporaba for ... else zanke (Najbolj "pythonovski" način)
Python ima posebno lastnost v zankah for. Če zanka teče do konca in se ne prekine z ukazom break, se takoj za tem izvede blok else.


## pregled - funkcija vse_nalozi
**Jaz**
kako recem pythonu naj pogleda ce je mapa prazna

**Gemini**
Če želiš v Pythonu preveriti, ali je mapa prazna, je najpreprostejši in najhitrejši način uporaba funkcije os.listdir().

Če seznam, ki ga vrne ta funkcija, ne vsebuje nobenega elementa, je mapa prazna.


## main - del ki pregleduje ce so spletne strani dostopne
**Jaz**
rada bi da ce website ni dostopen ne gleda kode naprej od tega 

**Gemini**
Če želiš, da program takoj preneha z izvajanjem in se ustavi, ko naleti na spletno stran, ki ni dosegljiva, moraš v zanki uporabiti ukaz break (in morda še sys.exit() ali pa preprosto prekiniti celotno izvajanje programa, da ne gre preverjat map in nalagat naprej).


## pregled - funkcija preveri vse podatke in preveri podatke
**Jaz**
ne daj mi kode, samo usmeri me kako lahko naredim da pregleda ce je 5 stolpcev v vsaki csv vrstici

**Gemini**
Za to ne potrebuješ nobene nove knjižnice. Ker že bereš vrstice iz datoteke (npr. z f.readlines()), lahko vsako prebrano vrstico preprosto razcepiš glede na ločilo (ki je v CSV datotekah običajno vejica).
Tvoja pot je torej takšna:
1. V zanki greš čez vsako prebrano vrstico v CSV datoteki.
2. Vrstico očistiš presledkov/skritih znakov na koncu (z metodu za besedila).
3. To vrstico razcepiš v seznam podatkov glede na vejico.
4. Z vgrajeno funkcijo preveriš dolžino tega nastalega seznama in preveriš, ali je enaka 5.
5. Če katera koli vrstica nima dolžine 5, funkcija takoj vrne False.


## hec - funkcija zahtevaj_opravicilo
**Jaz**
usmeri me kako napisem funkcijo, ki bo zahtevala da uporabnik napise doloceno stvar da se nadaljuje

**Gemini**
Zahteva, da uporabnik vpiše točno določeno besedo ali stavek za nadaljevanje programa, je klasična naloga v programiranju. Najlažje jo rešimo z zanko (while), ki se ponavlja, dokler vnos ni pravilen.

Python
def zahtevaj_vnos():
    # Določimo besedo, ki jo mora uporabnik vnesti
    pravilni_vnos = "naprej"

    while True:
        # Preberemo uporabnikov vnos in odstranimo odvečne presledke/nove vrstice
        uporabnikov_vnos = input(
            f"Za nadaljevanje vpiši besedo '{pravilni_vnos}': "
        ).strip()

        # Preverimo, ali se vnos ujema (ne glede na velike/male črke uporabimo .lower())
        if uporabnikov_vnos.lower() == pravilni_vnos:
            print("Uspešno! Nadaljujemo s programom...\n")
            break  # Prekine zanko in nadaljuje program
        else:
            print("Napačen vnos. Poskusi ponovno.")

Ključni gradniki kode:
input(): Omogoča branje vnosa, ki ga uporabnik tipka na tipkovnici.

.strip(): Odstrani začetne in končne presledke, če jih uporabnik pomotoma vpiše.

.lower(): Poskrbi, da vnos ni občutljiv na velike in male črke (tako "Naprej" kot "naprej" bosta delovala).

while True: Ustvari neskončno zanko, ki se vrti tako dolgo, dokler uporabnik ne vpiše pravilnega gesla in se izvede ukaz break.