# ivedu savaites diena skaiciumi  patikrinti ar tai darbo diena ar svaitgalis

diena = int(input('Kokia savaites diena? '))
viskasOk = True
match diena:
    case 1 | 2 | 3 | 4 | 5:
        txt = 'Darbo diena'

    case 6 | 7:
        txt = 'Savaitgalis'
    
    case _:
        print('Blogai įvesti duomenys')  #txt = 'Blogai įvesti duomenys'
        viskasOk = False
if viskasOk :
    print(f'{diena} - {txt}')