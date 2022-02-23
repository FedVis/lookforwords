#created using python 3.9.7
import tkinter
from tkinter import filedialog
from tkinter.messagebox import askyesno,showwarning
import os
from random import random
#from string import replace
#import string
from time import time

class main:
    
    lb=[]
    
    dices=([])

    dadi4=(['S','A','C','L','R','E'],
           ['E','A','T','I','O','A'],
           ['G','N','O','L','U','E'],
           ['I','S','E','E','F','H'],
           ['L','U','O','I','E','R'],
           ['N','E','D','O','S','T'],
           ['U','T','E','S','L','P'],
           ['R','A','T','I','B','L'],
           ['H','I','S','E','R','N'],
           ['M','P','A','C','E','D'],
           ['C','O','A','I','F','R'],
           ['A','M','S','R','I','O'],
           ['V','I','T','E','G','N'],
           ['D','A','N','E','Z','V'],
           ['N','O','E','U','C','T'],
           ['A','M','O','Qu','O','B'],)
    dadi5=(['Qu','O','M','B','A','O'],
           ['R','L','E','O','I','U'],
           ['C','O','A','I','R','F'],
           ['E','P','U','L','T','S'],
           ['T','O','I','D','V','M'],
           ['C','M','L','D','I','O'],
           ['H','N','S','R','E','I'],
           ['T','A','C','G','I','P'],
           ['E','D','O','N','T','S'],
           ['L','I','B','A','R','T'],
           ['G','F','A','I','R','P'],
           ['O','E','G','U','N','L'],
           ['U','C','O','T','N','E'],
           ['V','E','T','I','G','N'],
           ['E','A','T','I','O','A'],
           ['M','A','D','E','P','C'],
           ['E','H','I','F','S','E'],
           ['B','F','L','O','N','E'],
           ['A','L','E','R','C','S'],
           ['I','R','O','M','L','C'],
           ['C','P','V','A','S','G'],
           ['Z','E','V','A','N','D'],
           ['O','M','A','R','S','I'],
           ['Qu','S','B','Z','F','A'],
           ['O','C','A','M','I','B'],)
    try:
        fname=""
        fd=open('imp.txt','r')
        app=fd.readlines()
    except:
        #print("except dadi")
        w=5
        h=5
        font=50
        dices=dadi5
    else:
        fd.close()
        fname=app[0].replace('\n','')
        font=int(app[1].replace('\n',''))
    sw_salva=0

    def __init__(self):
        self.fin=tkinter.Tk()
        self.fin.title('Paroliere')
        menu=tkinter.Menu(self.fin)
        self.fin.config(menu=menu)
        menu.add_command(label='Help',command=self.help)
        self.fr=tkinter.Frame(self.fin)
        if self.fname!="":
            self.load_dices(self.fname)
        self.fr.grid()
        self.crea_lb()
        self.sv_time=tkinter.StringVar()
        self.sv_time.set('0')
        self.timer=tkinter.Label(self.fin,font=('',self.font//2),textvariable=self.sv_time)
        self.timer.grid(row=1)
        #print("stimer ",self.timer)
        self.nuovo(0)
        self.fin.bind('<F2>',self.nuovo)
        self.fin.bind('<F3>',self.cambia)
        self.fin.bind('<a>',self.ch_font)
        self.fin.bind('<z>',self.ch_font)
        #self.fin.bind('<Esc>',self.salva)
        self.fin.protocol("WM_DELETE_WINDOW",self.salva)        
        self.fin.mainloop()

    def crea_lb(self):
        #print("crea lb ",self.w," ",self.h)
        for x in self.lb:
            x.destroy()
        self.lb=[]
        for x in range(self.h):
            for y in range(0,self.w):
                self.lb.append(tkinter.Label(self.fr,font=('',self.font),bg='white',relief='sunken',borderwidth=1,text='A'))
                self.lb[-1].grid(row=x,column=y,sticky='nswe')

    def estrai_lettere(self):
        self.lettere=[]
        for x in self.dices:
            self.lettere.append(x[int(random()*len(x))])

    def estrai_posizione(self):
        for x in range(self.w*self.h-1,-1,-1):
            indice=int(random()*(x+1))
            #print indice
            self.lb[x].configure(text=' %s '%self.lettere[indice])
            del self.lettere[indice]
        #print 'lun',len(self.lettere)

    def nuovo(self,ev):
        self.estrai_lettere()
        self.estrai_posizione()
        self.time_start=time()
        self.contatore()

    def contatore(self):
        self.sv_time.set('%d'%(int(time()-self.time_start)))
        self.fin.after(1000,self.contatore)
        
    def genera(self):
        if "dices" not in os.listdir():
            os.mkdir("dices")
        if len(os.listdir("dices"))<2:
            #print("in os")
            f=open("dices/ITA-4X4.txt","w")
            f.write("""# lines starting with a "#" are comments
#this is the italian 4X4 set of dices, you can create your own set of dices
#Wide and Heigh, you could create not only 4X4 or 5X5 size... 
#8X6 for example is good but then you have to provide 64 dices
4X4
#write dices here down, they must be WxH and they could have more than 6 faces if you want
#following dices are the copy from the real italian board game but
#you can build your own set of dices and your preferred size
S,A,C,L,R,E
E,A,T,I,O,A
G,N,O,L,U,E
I,S,E,E,F,H
L,U,O,I,E,R
N,E,D,O,S,T
U,T,E,S,L,P
R,A,T,I,B,L
H,I,S,E,R,N
M,P,A,C,E,D
C,O,A,I,F,R
A,M,S,R,I,O
V,I,T,E,G,N
D,A,N,E,Z,V
N,O,E,U,C,T
A,M,O,Qu,O,B""")
            f.close()
            f=open("dices/ITA-5X5.txt","w")
            f.write("""5X5
Qu,O,M,B,A,O
R,L,E,O,I,U
C,O,A,I,R,F
E,P,U,L,T,S
T,O,I,D,V,M
C,M,L,D,I,O
H,N,S,R,E,I
T,A,C,G,I,P
E,D,O,N,T,S
L,I,B,A,R,T
G,F,A,I,R,P
O,E,G,U,N,L
U,C,O,T,N,E
V,E,T,I,G,N
E,A,T,I,O,A
M,A,D,E,P,C
E,H,I,F,S,E
B,F,L,O,N,E
A,L,E,R,C,S
I,R,O,M,L,C
C,P,V,A,S,G
Z,E,V,A,N,D
O,M,A,R,S,I
Qu,S,B,Z,F,A
O,C,A,M,I,B""")
            f.close()
        fname=filedialog.askopenfilename(initialdir = "dices",title = "Select file",filetypes = (("text","*.txt"),("all files","*.*")))
        #print(fname)
        self.load_dices(fname)
        
    def load_dices(self,fn):
        f=open(fn,"r")
        lines=f.readlines()
        f.close()
        self.w=0
        self.h=0
        for x in range(len(lines)):
            l=lines[x].replace(" ","").replace("\n", "")
            if l[0]!="#":
                #set the size w and h from the file
                if self.w==0 or self.h==0:
                    if "X" in l:
                        self.w,self.h=map(int,l.split("X"))
                        #print("w ",self.w," h ",self.h," ",type(self.w))
                        self.dices=[]
                else:
                    self.dices.append(l.split(","))
        if len(self.dices)!=self.w*self.h:
            print("wrong number of dices")
        else:
            self.dices=tuple(self.dices)
            #print(self.w,"  ",self.h,"\ndices caricati\n", len(self.dices),"\n",self.dices)
        self.fname=fn
    
    def cambia(self,ev):
        #verifico se esiste una cartella dices e in caso la creo e genero i file per i dadi ita
        self.genera()
        ###
        self.sw_salva=1
        #fname=filedialog.askopenfilename(initialdir = "dices",title = "Select file",filetypes = (("text","*.txt"),("all files","*.*")))
        #self.load_dices(fname)
        self.crea_lb()
        self.nuovo(0)

    def ch_font(self,ev):
        self.sw_salva=1
        if ev.keysym=='a':
            if self.font<250:
                self.font+=1
        else:
            if self.font>1:
                self.font-=1
        for x in self.lb:
            x.configure(font=('',self.font))
        self.timer.configure(font=('',self.font//2))

    def salva(self):
        if self.sw_salva:
            if askyesno('Save','save settings?'):
                fd=open('imp.txt','w')
                fd.write('%s\n%d\n'%(self.fname,self.font))
                fd.close()
        self.fin.destroy()

    def help(self):
        showwarning('Help',"""F2 --> New Game
F3 Load Dices
"A" or "Z" to increase or reduce font size

Use this program for free,
Author: Federico Visconti""")
            

####main###
if __name__=='__main__':
    App=main()
