#Vinis
import math
viniesIlgis = int(input('Kokio ilgio vinis centimetrais? '))
likutis = viniesIlgis
k = float(input('Kiek cm vinies ikalama? '))
for i in range(1, int(math.ceil(viniesIlgis/k)+1)):
    likutis = round(likutis - k,2)
    if likutis > 0:
         print(f'"Tuk!" {i}-asis smugis. Dar liko {likutis} cm neikaltos vinies')
    else:
         print(f'"Tuk!" {i}-asis smugis. Vinis ikalta')
        