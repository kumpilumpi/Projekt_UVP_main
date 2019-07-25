#tekstovni vmesnik za xoxo.py

import xoxo
import os

clear = lambda: os.system('cls')
lojtrice = "#################################"



def zacni_igro():
    igra_1 = xoxo.Igra()
    
    while not igra_1.zmaga() and igra_1.poteze < 82:
        natisni_mreza(igra_1)
        print('Na potezi je {}'.format(igra_1.navrsti))
        print(lojtrice)
        vrsta = input('Vrsta: ')
        stolpec = input('Stolpec: ')
        igra_1.poteza(int(vrsta), int(stolpec))
        
        clear()

    natisni_mreza(igra_1)
    print(lojtrice)

    if igra_1.zmaga():
        igra_1.O_X()
        print('Zmagovalec je {}'.format(igra_1.navrsti))
        _ = input('Za izhod pritisnite enter!  ')
    else:
        print('Oba sta zmagovalca!')

def natisni_mreza(objekt):
    for vrsta in objekt.mreza:
        print(' {} \n'.format(vrsta) )

zacni_igro()
 



