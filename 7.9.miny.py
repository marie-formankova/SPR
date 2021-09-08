from random import*

class Hra:
    def __init__(self):
        self.p = self.pole()
        self.hra = self.tah(self.pole)

    def n_list(self, n):
        return [0]*n

    def end(self):
        print('GAME OVER:(')

    def zobr_pole(self, pole):
        print('\n\n')
        self.prohra = False
        for radek in self.pole:
            self.c=0
            for n in radek:
                if self.c==j-1:
                    if n is not None and n>0:
                        print(f' {min(2,self.count-1)} ')
                        n=self.count-1
                    elif n is not None and n<0:
                        print(' * ')
                        self.prohra =True
                    else: 
                        print(' . ')
                else:
                    if n is not None and n>0:
                        print(f' {min(self.count-1,2)} ', end = '')
                        n=self.count-1
                    elif n is not None and n<0:
                        print(' * ', end='')
                        self.prohra =True
                    else:
                        print(' . ', end='')
                    self.c+=1
        if self.prohra==True: self.end()
        print('\n\n')  
        self.tah(pole)       

    def pole(self):
        self.pole=[]
        global j
        j=6
        for _ in range(j):
            radek = self.n_list(j)
            self.pole.append(radek)
       
        self.i = 2
        while self.i>0:
            self.rand1=randint(0,3)
            self.rand2=randint(0,3)
            self.mina =self.pole[self.rand1][self.rand2]
            
            if self.mina==None:
                self.mina = None
            else:
                self.mina=None
                self.pole[self.rand1][self.rand2]=self.mina
                self.i=self.i-1
        print(self.pole) 
        #zobrazi skryty dvourozmerny seznam min a volnych poli
        self.zobr_pole(self.pole)
        return self.pole

    def nepl_tah(self, pole):
        print('\n\n')
        print('TYTO SOUŘADNICE JSOU NEPLATNÉ\n')
        self.tah(pole)

    def game_over(self,pole,a,b):
        self.pole[a][b] = -1
        self.zobr_pole(pole)

    def hraci_pole(self, pole, a, b):
        if pole[a][b] is None:
            self.game_over(pole,a,b)
        self.neighbors= [pole[max(0, a-1)][max(0,b-1)],pole[a][max(0,b-1)], pole[min(j-1, a+1)][max(0,b-1)],pole[max(0, a-1)][b],pole[max(0, a-1)][max(0,b-1)],pole[min(a+1,j-1)][b], pole[max(0, a-1)][min(j-1,b+1)], pole[a][min(j-1,b+1)],pole[min(j-1, a+1)][min(j-1,b+1)]]
        self.count = sum(x is None for x in self.neighbors)+1

        pole[a][b] = self.count
        self.zobr_pole(pole)

    def tah(self, pole):
        self.inp = input(f'Zadej souřadnice (0 až {j-1} ):  řádek,sloupec\n')
        try:
            self.a = int(self.inp[0])
            self.b = int(self.inp[-1])
        except:
            self.nepl_tah(pole)
        if self.a not in range(j) or self.b not in range(j):
            self.nepl_tah(pole)

        self.hraci_pole(pole, self.a, self.b)
       
        
       
k = Hra()
