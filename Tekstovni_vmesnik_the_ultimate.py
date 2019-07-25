#tesktovni vmesnik za model_the_ultiate_game.py

#če klikne enter na prazen vnos vrže vn

import model
import os

lojtrice = "#####################################################"
clear = lambda: os.system('cls')

def zacni_igro_igralca():
    igra = model.The_ultimate_game()

    igra.mreza_natisni()
    print(lojtrice)
    print('Na potezi je {}'.format(igra.navrsti))
    mreza = input('Mreza: ')
    vrsta = input('Vrsta: ')
    stolpec = input('Stolpec: ')
    clear()


    while not igra.velika_zmaga() and not igra.velika_je_polna():
        try: #ker ko je bil na input kliknjen enter je prišlo do napake (pretvorba v int) in se je igra končala
            if igra.dobr_vnos(int(mreza)-1, int(vrsta)-1, int(stolpec)-1):
                igra.poteza(int(mreza)-1, int(vrsta)-1, int(stolpec)-1) 
                igra.mreza_natisni()
                print(lojtrice)
                if igra.mreza_naslednja != 10:
                    print('Na potezi je {}'.format(igra.navrsti))
                    print('Igrate v mrezo {}.'.format(igra.mreza_naslednja + 1))
                    mreza = igra.mreza_naslednja + 1
                    vrsta = input('Vrsta: ')
                    stolpec = input('Stolpec: ')
                    clear()
                else:
                    print('Na potezi je {}'.format(igra.navrsti))
                    mreza = input('Mreza: ')
                    vrsta = input('Vrsta: ')
                    stolpec = input('Stolpec: ')
                    clear()
                    
            else:
                igra.mreza_natisni()
                print(lojtrice)
                print('Neveljavna poteza! \nPoskusite ponovno ali preberite navodila.')
                if igra.mreza_naslednja == 10:
                    print('Na potezi je {}'.format(igra.navrsti))
                    mreza = input('Mreza: ')
                    vrsta = input('Vrsta: ')
                    stolpec = input('Stolpec: ')
                    clear()
                else:
                    print('Na potezi je {}'.format(igra.navrsti))
                    print('Igrate v mrezo {}.'.format(igra.mreza_naslednja + 1))
                    mreza = igra.mreza_naslednja + 1
                    vrsta = input('Vrsta: ')
                    stolpec = input('Stolpec: ')
                    clear()
        except:
            igra.mreza_natisni()
            print(lojtrice)
            print('Neveljavna poteza! \nPoskusite ponovno ali preberite navodila.')
            if igra.mreza_naslednja == 10:
                print('Na potezi je {}'.format(igra.navrsti))
                mreza = input('Mreza: ')
                vrsta = input('Vrsta: ')
                stolpec = input('Stolpec: ')



                clear()
            else:
                print('Na potezi je {}'.format(igra.navrsti))
                print('Igrate v mrezo {}.'.format(igra.mreza_naslednja + 1))
                mreza = igra.mreza_naslednja + 1
                vrsta = input('Vrsta: ')
                stolpec = input('Stolpec: ')
                clear()

    #Ko se igra konca

    if igra.velika_zmaga():
        igra.mreza_natisni()
        print(lojtrice)
        igra.naslednji()
        print('Zmagal je {}.'.format(igra.navrsti))
        print('Hvala, da ste igrali.')
        _ = input('Za izhod pritisnite enter.')
    else:
        igra.mreza_natisni()
        print(lojtrice)
        print('Igra je bila neodlocena.')
        print('Hvala, da ste igrali.')
        _ = input('Za izhod pritisnite enter.')

        

            




zacni_igro_igralca()
