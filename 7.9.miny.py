from random import*

class Hra:
    def __init__(self):
        self.p = self.pole()
        self.hra = self.tah(self.pole)

    def n_list(self, n):
        return [0]*n

    def zobr_pole(self, pole):
        for radek in self.pole:
            self.c=0
            for n in radek:
                if self.c==3:
                    if n==0 or n==1:
                        print(' . ')
                    if n==2:
                        print(' * ')
                    if n<0:
                        print(' O ' )
                else:
                    if n==0 or n==1:
                        print(' . ', end='')
                    if n==2:
                        print(' * ', end='')
                    if n<0:
                        print(' O ', end='' )
                    self.c+=1

        self.tah(self.pole)
                

    def pole(self):
        self.pole=[]
        n=4
        for _ in range(n):
            radek = self.n_list(n)
            self.pole.append(radek)
       
        self.i = 2
        while self.i>0:
            self.rand1=randint(0,3)
            self.rand2=randint(0,3)
            self.mina =self.pole[self.rand1][self.rand2]
            
            if self.mina==1:
                self.mina = 1
            else:
                self.mina=self.mina+1
                self.pole[self.rand1][self.rand2]=self.mina
                self.i=self.i-1
        print(self.pole)
        self.hraci_pole = self.zobr_pole(self.pole)
        return self.pole

    
    def tah(self, pole):
        self.inp = input('Zadej souřadnice (0 až 3):  řádek,sloupec\n')
        self.a = int(self.inp[0])
        self.b = int(self.inp[-1])
        print(self.a,'   ',self.b)
        self.t =pole[self.a][self.b]
        self.t+=1
        if self.t==1:
            pole[self.a][self.b]=-1
        else:
            pole[self.a][self.b]=self.t

        self.zobr_pole(pole)

k = Hra()
