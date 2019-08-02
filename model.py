#The Ultimate tictac game


class The_ultimate_game:

    def __init__(self):
        
        self.mala_mreza_0 = self.mala_mreza_ustvari()
        self.mala_mreza_1 = self.mala_mreza_ustvari()
        self.mala_mreza_2 = self.mala_mreza_ustvari()
        self.mala_mreza_3 = self.mala_mreza_ustvari()
        self.mala_mreza_4 = self.mala_mreza_ustvari()
        self.mala_mreza_5 = self.mala_mreza_ustvari()
        self.mala_mreza_6 = self.mala_mreza_ustvari()
        self.mala_mreza_7 = self.mala_mreza_ustvari()
        self.mala_mreza_8 = self.mala_mreza_ustvari()

        self.mreza_zadnja = None
        self.mreza_naslednja = 10   #10 pomeni, da gre lahko v katerokoli mrežo
        self.vrsta_zadnja = None
        self.stolpec_zadnja = None
        self.navrsti = 'X'
        self.velika_mreza = [self.mala_mreza_0, self.mala_mreza_1, self.mala_mreza_2, self.mala_mreza_3 ,self.mala_mreza_4, self.mala_mreza_5, self.mala_mreza_6, self.mala_mreza_7, self.mala_mreza_8]

        self.slaba = False #za bottle_vmesnik

    def mala_mreza_ustvari(self): #dela
        'Ustvari mrezo 3*3.'
        mreza_n = []
        for _ in range(3):
            mreza_n.append(['-', '-', '-'])
        return mreza_n
    
    def mreza_natisni(self): #dela
        'Natisne veliko mrezo.'
        for i in range(3):
            print('{}, | {}, | {} \n'.format(self.mala_mreza_0[i], self.mala_mreza_1[i], self.mala_mreza_2[i]))
        print('-----------------------------------------------------')
        for i in range(3):
            print('{}, | {}, | {} \n'.format(self.mala_mreza_3[i], self.mala_mreza_4[i], self.mala_mreza_5[i]))
        print('-----------------------------------------------------')
        for i in range(3):
            print('{}, | {}, | {} \n'.format(self.mala_mreza_6[i], self.mala_mreza_7[i], self.mala_mreza_8[i]))
    
    def dobr_vnos(self, mreza, vrsta, stolpec): #dela
        'Preveri, če je vnos dobr. Preveri, da je izbrana 0, da so parametri vredu in da noben ni na mreži še zmagal.'
        try:
            if (vrsta < 3) and (stolpec < 3) and (mreza < 9) and (self.velika_mreza[mreza][vrsta][stolpec] == '-'):
                self.slaba = False #sprememba za bottle vmesnik
                return True 
            else:
                self.slaba = True
                return False
        except: # Ker drgac javlja list index out of range ali če index ni dobr (npr. ni stevilka)
            self.slaba = True
            return False
        
    def polna_mreza(self, mreza, nastavi): #dela
        'Vse člene te mreže postavi na nastavi.'
        for vrsta in self.velika_mreza[mreza]:
            for i in range(3):
                vrsta[i] = nastavi
    
    def mala_neodloceno(self, mreza): #dela
        'Preveri če je mala mreza neodlocena.'
        return True if (self.je_polna(mreza) and not self.mala_zmaga(mreza)) else False
    
    def mala_zmaga(self, mreza): #dela
        'Preveri, če so kje v mali mrezi 3 v vrsto.'
        for i in range(3): 
            if ((self.velika_mreza[mreza][i][0] != '-') and (self.velika_mreza[mreza][i][0] == self.velika_mreza[mreza][i][1] == self.velika_mreza[mreza][i][2])) or ((self.velika_mreza[mreza][0][i] != '-') and (self.velika_mreza[mreza][0][i] == self.velika_mreza[mreza][1][i] == self.velika_mreza[mreza][2][i])): 
                return True
        if (self.velika_mreza[mreza][1][1] != '-') and (self.velika_mreza[mreza][0][0] == self.velika_mreza[mreza][1][1] == self.velika_mreza[mreza][2][2]): 
             return True 
        elif (self.velika_mreza[mreza][1][1] != '-') and (self.velika_mreza[mreza][0][2] == self.velika_mreza[mreza][1][1] == self.velika_mreza[mreza][2][0]):
            return True
        else:
            return False

    def mala_nastavi(self, mreza): #dela 
        'Preveri za mrezo, ce je neodloceno, potem nastavi vse clene na /, ce je kdo zmagal, nastavi vse clene na zamagovalca'
        if self.mala_zmaga(mreza): 
            self.polna_mreza(mreza, self.navrsti)
        elif self.mala_neodloceno(mreza):
             self.polna_mreza(mreza, '/')

    def je_polna(self, mreza): #dela
        'Preveri če je mreža polna - vsi členi različni od 0.'
        for vrsta in self.velika_mreza[mreza]:
            for clen in vrsta:
                if clen == '-':
                    return False
        return True

    def naslednji(self): #dela
        'Premakne za eno naprej kdor je navrsti'
        self.navrsti = 'X' if self.navrsti == 'O' else 'O'
    
    def poteza(self, mreza, vrsta, stolpec):  #dela
        'Naredi potezo, nastavi kam se je igralo nazadnje, spremni igralca, preveri mala_zmaga() in mala_neodloceno...'
        self.mreza_zadnja = mreza
        self.vrsta_zadnja = vrsta
        self.stolpec_zadnja = stolpec
        self.velika_mreza[mreza][vrsta][stolpec] = self.navrsti
        self.mala_nastavi(mreza)
        self.naslednji()
        self.naslednja_poteza()

    def naslednja_poteza(self): #dela
        'Doloci v katero mrežo se igra naslednje.'
        if not self.je_polna(0) and self.vrsta_zadnja == self.stolpec_zadnja == 0:
                self.mreza_naslednja = 0
        elif not self.je_polna(1) and self.vrsta_zadnja == 0 and self.stolpec_zadnja == 1:
                self.mreza_naslednja = 1
        elif not self.je_polna(2) and self.vrsta_zadnja == 0 and self.stolpec_zadnja == 2:
                self.mreza_naslednja = 2
        elif not self.je_polna(3) and self.vrsta_zadnja == 1 and self.stolpec_zadnja == 0:
                self.mreza_naslednja = 3
        elif not self.je_polna(4) and self.vrsta_zadnja == self.stolpec_zadnja == 1:
                self.mreza_naslednja = 4
        elif not self.je_polna(5) and self.vrsta_zadnja == 1 and self.stolpec_zadnja == 2:
                self.mreza_naslednja = 5
        elif not self.je_polna(6) and self.vrsta_zadnja == 2 and self.stolpec_zadnja == 0:
                self.mreza_naslednja = 6
        elif not self.je_polna(7) and self.vrsta_zadnja == 2 and self.stolpec_zadnja == 1:
                self.mreza_naslednja = 7
        elif not self.je_polna(8) and self.vrsta_zadnja == self.stolpec_zadnja == 2:
                self.mreza_naslednja = 8
        else:
                self.mreza_naslednja = 10
   
    def velika_zmaga(self): #dela
        'Preveri, če je kdo zmagal.'
        for i in range(3):
            if self.je_polna(0 + i*3) and self.je_polna(1 + i*3) and self.je_polna(2 + i*3) and (self.velika_mreza[0 + i*3][0][0] == self.velika_mreza[1 + i*3][0][0] == self.velika_mreza[2 + i*3][0][0] != '/'):
                return True
            elif self.je_polna(0 + i) and self.je_polna(3 + i) and self.je_polna(6 + i) and (self.velika_mreza[0 + i][0][0] == self.velika_mreza[3 + i][0][0] == self.velika_mreza[6 + i][0][0] != '/'):
                return True
        if self.je_polna(0) and self.je_polna(4) and self.je_polna(8) and (self.velika_mreza[0][0][0] == self.velika_mreza[4][0][0] == self.velika_mreza[8][0][0] != '/'):
            return True
        elif self.je_polna(2) and self.je_polna(4) and self.je_polna(6) and (self.velika_mreza[2][0][0] == self.velika_mreza[4][0][0] == self.velika_mreza[6][0][0] != '/'):
            return True                
        else:
            return False
    
    def velika_je_polna(self): #dela
        'Preveri, če je igra neodlocena.'
        for i in range(9):
            if not self.je_polna(i):
                return False
        else: 
            return True  





class Igra_xo:
    def __init__(self):
        self.igre = [] 
        # self.slaba = False  # je že slaba v classu The_ultimate_game

    def prost_id_igre(self):
        return 0 if len(self.igre) == 0 else len(self.igre)
                
    def nova_igra(self):
        id_igre = self.prost_id_igre()
        igra = The_ultimate_game()
        self.igre.append(igra)
        return id_igre

    def poteza_db_sl(self, id_igre, mreza, vrsta, stolpec):
        'Preveri, če je poteza dobra, jo naredi spremeni slaba v False, ali  če je poteza slaba spremeni slaba v True.'
        igra = self.igre[id_igre]
        if igra.dobr_vnos(mreza, vrsta, stolpec):
            igra.poteza(mreza, vrsta, stolpec)
            # igra.slaba =  False
            self.igre[id_igre] = igra
            return
        else:
            igra.slaba = True       
            self.igre[id_igre] = igra
            return

    def zmaga(self, id_igre): 
        'Preveri, če je zmaga.'
        igra = self.igre[id_igre]
        return igra.velika_zmaga()
    
    def mreza_naslednja_2(self, id_igre): #ker se spremenljivke v bottlu ne prepošljejo 
        'V katero mrežo se igra naslednje.'
        igra = self.igre[id_igre]
        return igra.mreza_naslednja

    def slaba_fun(self, id_igre):
        'Vrne atribut slaba od igra.'
        igra = self.igre[id_igre]
        return igra.slaba



    # def prosto_omejeno(self, id_igre): #enkrat napisu zaenkrat  ne rabim neikjer drugje
    #     'Preveri, naslednjo potezo.'
    #     igra = self.igre[id_igre]
    #     return igra.naslednja_mreza()


# igra = Igra_xo()
# moj_id_igre = igra.nova_igra()
# print(igra.igre[moj_id_igre])
# print(igra.poteza_db_sl(moj_id_igre, 1, 1, 1))
# print(igra.igre[moj_id_igre])
# print(igra.igre)
# print(igra.igre[moj_id_igre].mreza_natisni())





# igra = The_ultimate_game()

# igra.polna_mreza(0, igra.navrsti)
# igra.polna_mreza(3, igra.navrsti)
# igra.polna_mreza(6, igra.navrsti)
# igra.mreza_natisni()
# print(igra.velika_zmaga())

# igra.poteza(0,0,0)
# igra.poteza(0,1,1)
# igra.poteza(0,2,2)
# igra.poteza(0,2,1)
# igra.poteza(0,0,1)
# igra.poteza(0,0,2)
# igra.poteza(0,2,0)
# igra.poteza(0,1,0)
# igra.poteza(0,1,2)

# print(igra.mala_mreza_0)
# print(igra.dobr_vnos(0,1,0))

# print(igra.je_polna(0))
# print(igra.mala_zmaga(0))
# print(igra.mala_neodloceno(0))

# print(igra.mala_zmaga(0))
# igra.polna_mreza(0, igra.navrsti)
# igra.mala_nastavi(2)

# #print(igra.dobr_vnos(0,0,0))
# igra.mreza_natisni()
# print(igra.mala_zmaga(0))
# igra.polna_mreza(3)
# igra.naslednji()
# igra.polna_mreza(4)
# igra.mreza_natisni()
# print(igra.navrsti)
# igra.naslednji()
# print(igra.navrsti)

