from random import*

class Hra:
    def __init__(self):
        self.p = self.pole()
        self.prpole()
        self.hra = self.tah()    
    
    def prpole(self):
        c = 0
        for n in range(36):
            if c ==5:
                print(' . ')
                c=0
            else:
                print(' . ',end='')
                c+=1

    def pole(self):
        self.hpole = {}
        self.n = 36
        for self.n in range(self.n):
            self.hpole[self.n] = 0
        m=3
        while m>0:
            self.mina = randint(0,self.n)
            if self.hpole[self.mina] ==None:
                pass
            else:
                self.hpole[self.mina] = None
                m=m-1
                self.add_ns(self.mina)
        print(self.hpole)
        
    def add_ns(self, mina):
        self.sousedi =[-7,-6,-5,-1,1,5,6,7]
        for l in self.sousedi:
            try:
                self.hpole[mina+l]+=1
            except:
                k=1

    def zobr(self):
        c = 0
        for n in range(36):
            if c ==5:
                if self.hpole[n]==None:
                    if self.prohra == True:
                        print(' * ')
                    else:
                        print(' . ')
                elif self.hpole[n]<1000:
                    print(' . ')
                else:
                    self.g =self.hpole[n]//1000
                    print(f' {self.hpole[n]-self.g*1000} ')
                c=0
            elif c <5:
                if self.hpole[n]==None:
                    if self.prohra == True:
                        print(' * ',end='')
                    else:
                        print(' . ',end='')
                elif self.hpole[n]<1000:
                    print(' . ',end='')
                else:
                    self.g =self.hpole[n]//1000
                    print(f' {self.hpole[n]-self.g*1000} ',end='')
                c+=1
        if self.prohra==True:
            self.end()
        else:
            self.tah()
        
    def end(self):
        print('\n\nŠLÁPLI JSTE NA MINU. HRA SKONČILA!\n\n')

    def tah(self):
        self.inp1 = input('Zadej souřadnici řádku (0 až 5 ):\n')
        self.inp2 = input('Zadej souřadnici sloupce (0 až 5 ):\n')
        try:
            self.a = int(self.inp1[0])
            self.b = int(self.inp2[0])
        except:
            self.nepl_tah()
        if self.a not in range(6) or self.b not in range(6):
            self.nepl_tah()

        self.key = self.a*6+self.b
        if self.hpole[self.key]==None:
            self.prohra=True
        else:
            self.hpole[self.key] = self.hpole[self.key]+1000
            self.prohra = False

        self.zobr()

    def nepl_tah(self):
        print('\n\n')
        print('TYTO SOUŘADNICE JSOU NEPLATNÉ\n')
        self.tah()

k = Hra()
