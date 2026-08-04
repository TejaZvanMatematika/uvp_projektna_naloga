# uvp_projektna_naloga

## opis
To je program ki shrani HTML kodo iz spletne strani FIDE, potem iz te kode
izlušči podatke, in te podatke shrani v csv datoteko. Vse datoteke so urejene
po mapah za lažjo berljivost. Program je narejen tako da preveri delovanje spletnih
strani in sporoči napako. Program tudi preverja dolžino csv in število stolpcev,
tako da če kaj ni vredu ponovno naloži le določen csv ne pa vseh.
Program ima tudi vključeno šalo, in sicer če je že vse naloženo uporabnik pa še
vedno zaganja program, bo po parih ponovitvah nekaj rekel, po stotih pa bo program
izbrisal datoteke (html in csv) in od uporabnika zahteval opravičilo.


## uporaba
1.  uporabnik naj najprej naloži vse potrebne datoteke iz Git reposetorija
    (preko terminala z 'git clone <https od reposetorija>' command ali pa
    naj v reposetoriju pritisne Code<> in spodaj download ZIP, potem pa naj
    to datoteko razširi v mapo).

2.  naložen naj ima urejevalnik ki podpira python (npr. VScode), po potrebi pa
    naj še naloži python (najbolje je če je najnovejši).

3.  preveri naj če mu vse knjižnice delujejo (re, os, sys, ...), po potrebi
    jih namesti.

4.  Zagon programa:
    VScode: uporabnik naj odpre datoteko in pritisne trikotnik desno zgoraj
    (Run Python File)
    Terminal: uporabnik naj v terminal napise 'python main.py'