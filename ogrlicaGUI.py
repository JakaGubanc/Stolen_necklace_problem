
from tkinter import *


import math
from tkinter.colorchooser import *


def razdelitev_na_k_delov(s,m):
    if len(s)==m:
        return [[[i] for i in s]]
    if m == 1:
        return [[s]]
    else:
        razdelitve = []
        for i in range (1,len(s)-m+2):
            for j in razdelitev_na_k_delov(s[i:],m-1):
                temp = j[::-1]+[s[:i]]
                razdelitve = razdelitve + [temp[::-1]]
        return razdelitve


def je_postena(delitev, znaki):
    presteto = dict()
    for i in znaki:
        presteto[i] = [0,0] 
    for i in range(len(delitev)):
        for j in delitev[i]:
            if i%2 == 0:
                presteto[j][0] += 1
            else:
                presteto[j][1] += 1
    for i in presteto:
        if presteto[i][0] != presteto[i][1]:
            return False
        
    return True


def postena_delitev(s):
    postene=[]
    znaki = set()
    for i in s:
        znaki.add(i)
    k = len(znaki)
    for delitev in razdelitev_na_k_delov(s,k+1):
        if je_postena(delitev, znaki):
            #return delitev
            postene.append(delitev)
    return postene

#for i in postena_delitev(['red', 'blue', 'blue', 'green', 'green', 'red']):
 #   print(i)





class OgrlicaGUI():
    def __init__(self, master):
        self.ogrlica = []
        self.d=45
        self.off= 650 - len(self.ogrlica)*22.27
        self.r = 30

        self.canvas = Canvas(master, width=1300, height=300, bg = 'white')
        self.canvas.grid(row=0, columnspan=25)
    

        d1 = Button(master,width=3, bg='blue', command=self.narisi_dragulj_barve('blue'))
        d1.grid(row=1,column=10)
        d2 = Button(master, width=3, bg='red', command=self.narisi_dragulj_barve('red'))
        d2.grid(row=1,column=11)
        d3 = Button(master, width=3, bg='green', command=self.narisi_dragulj_barve('green'))
        d3.grid(row=1,column=12)
        d4 = Button(master, width=3, bg='purple', command=self.narisi_dragulj_barve('purple'))
        d4.grid(row=1,column=13)
        d5 = Button(master, width=3, bg='orange', command=self.narisi_dragulj_barve('orange'))
        d5.grid(row=1,column=14)

        posteno_razdeli = Button(master, text='POSTENA DELITEV', command=self.posteno_razdeli  )
        posteno_razdeli.grid(row=2,column=12)
       
        ponovno_narisi_gumb = Button(master, text='PONOVNO NARIŠI', command=self.ponovno_narisi  )
        ponovno_narisi_gumb.grid(row=3,column=12)
       
       
        menu = Menu(master)
        
        master.config(menu=menu)
        menu.add_command(label="Končaj", command=master.destroy)
        menu.add_command(label="Počisti", command=self.pocisti)
    
    def ponovno_narisi(self):
        self.canvas.delete(ALL)
        j = 0
        for barva in self.ogrlica:
            self.canvas.create_polygon(15+j*self.d+self.off,150,30+j*self.d+self.off,15+150,15+j*self.d+self.off,30+150,0+j*self.d+self.off,15+150,fill=barva,)
            if j != len(self.ogrlica)-1:
                self.canvas.create_line(30+j*self.d+self.off,15+150,0+(j+1)*self.d+self.off,15+150)
            j = j + 1

    def narisi_dragulj_barve(self,trenutna_barva):
        def narisi_dragulj(barva=trenutna_barva):
            self.canvas.delete('all')
            self.ogrlica.append(barva)
            self.off= 650 - len(self.ogrlica)*22.27
            j = 0
            for barva in self.ogrlica:
                #self.canvas.create_line(100,110,100,90,width=2)
                #self.canvas.create_line(100 + j*self.d,100,100 + (j+1)*self.d,100,fill=barva,width=4)
                #self.canvas.create_line(100+(j+1)*self.d,110,100+(j+1)*self.d,90,width=2)
                self.canvas.create_polygon(15+j*self.d+self.off,150,30+j*self.d+self.off,15+150,15+j*self.d+self.off,30+150,0+j*self.d+self.off,15+150,fill=barva,)
                if j != len(self.ogrlica)-1:
                    self.canvas.create_line(30+j*self.d+self.off,15+150,0+(j+1)*self.d+self.off,15+150)
                j = j + 1

        return narisi_dragulj

    def posteno_razdeli(self):
        self.canvas.delete(ALL)
        print(postena_delitev(self.ogrlica))
        j = 0
        posteno = postena_delitev(self.ogrlica)[len(postena_delitev(self.ogrlica))//2]
        for i in range(len(posteno)):
            k = 0
            for barva in posteno[i]:
                if i%2 == 0:
                    self.canvas.create_polygon(15+j*self.d+self.off,150-self.r,30+j*self.d+self.off,15+150-self.r,15+j*self.d+self.off,30+150-self.r,0+j*self.d+self.off,15+150-self.r,fill=barva,)
                    if k != len(posteno[i])-1:
                        self.canvas.create_line(30+j*self.d+self.off,15+150-self.r,0+(j+1)*self.d+self.off,15+150-self.r)
                else:
                    self.canvas.create_polygon(15+j*self.d+self.off,150+self.r,30+j*self.d+self.off,15+150+self.r,15+j*self.d+self.off,30+150+self.r,0+j*self.d+self.off,15+150+self.r,fill=barva,)
                    if k != len(posteno[i])-1:
                        self.canvas.create_line(30+j*self.d+self.off,15+150+self.r,0+(j+1)*self.d+self.off,15+150+self.r)
                k = k+1
                j = j + 1
            if i != len(posteno)-1:
                self.canvas.create_line(15+j*self.d+self.off-23,150-self.r-20,15+j*self.d+self.off-23,150+self.r+45)

    def pocisti(self):

        self.canvas.delete(ALL)
        self.ogrlica =[]

    
                
                


root = Tk()

aplikacija = OgrlicaGUI(root)

root.mainloop()
