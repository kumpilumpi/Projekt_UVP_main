#Križci in krožci igra



class Igra:

    def __init__(self):

        self.navrsti = 'X'
        # self.vrsta_M = 0       -> Če bi sprogramiru mal boljš zmaga()
        # self.stolpec_M = 0
        self.mreza = self.mreza_ustvari()
        self.poteze = 0


    def mreza_ustvari(self):
        mreza_n = []
        for _ in range(3):
            mreza_n.append([0, 0, 0])
        return mreza_n

    def O_X(self): 
        'Premakne za eno naprej kdor je navrsti'
        if self.navrsti == 'X':
            self.navrsti = 'O'
        else: 
            self.navrsti = 'X'

    def dobr_vnos(self, vrsta, stolpec):
        if vrsta > 2 or stolpec > 2:
            return False
        else: 
            return True
           
    def poteza(self, vrsta, stolpec):
        'Če je poteza ok jo naredi in vrne True, drgač vrne False'
        # self.vrsta_M = vrsta
        # self.stolpec_M = stolpec
        
        if self.dobr_vnos(vrsta, stolpec) and self.mreza[vrsta][stolpec] == 0:
            self.mreza[vrsta][stolpec] = self.navrsti
            self.O_X()
            self.poteze += 1
            return True         
        else:
           return False

    def zmaga(self): 
        'Preveri če so kje 3 v vrsti'
        for i in range(3):
            if ((self.mreza[i][0] != 0) and (self.mreza[i][0] == self.mreza[i][1] == self.mreza[i][2])) or ((self.mreza[i][0] != 0) and (self.mreza[0][i] == self.mreza[1][i] == self.mreza[2][i])): 
                return True
            
            elif ((self.mreza[1][1] != 0)) and ((self.mreza[0][0] == self.mreza[1][1] == self.mreza[2][2]) or (self.mreza[0][2] == self.mreza[1][1] == self.mreza[2][0])): 
                return True
            
            else:
                return False
        



        
        

            
# def zacni_igro():
#     return Igra()
#     igra_1.mreza_ustvari()
#     while igra_1.zmaga:
#         print(igra_1.mreza)
#         print('Na potezi je {}'.format(igra_1.navrsti))
#         vrsta = input('Vrsta: ')
#         stolpec = input('Stolpec: ')
#         igra_1.poteza(int(vrsta), int(stolpec))
#         igra_1.zmaga()
    
#     print('Izgubil je {}'.format(igra_1.navrsti))



    
