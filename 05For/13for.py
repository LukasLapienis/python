# Kartais žmonėms būna sunku prisiminti, kokia šiandien yra savaitės diena, o ir 
# kalendorius ne visada būna po ranka. Parašykite programą, kuri išspausdintų 
# vieno mėnesio savaitės dienų sąrašą nuo a dienos iki b dienos, jei žinoma, 
# kad mėnuo prasidėjo m-tąją savaitės dieną. Savaitės dienos numeruojamos taip: 
# 1-pirmadienis, 2-antradienis ... 7 - sekmadienis.

savDiena = int(input('Kokia  savaites diena prasideda menuo? '))
a =int(input('Nuo kurios dienos prasideda? ')) 
b =int(input('Kuria diena pasibaigia? ')) 
for i in range(1, 32):
    if a<=i<=b:
        print(f'{i}-oji diena: {savDiena}')
    if savDiena == 7:
        savDiena = 1
    else:
        savDiena += 1
    if i==b:
        break
