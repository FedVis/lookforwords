import Tkinter
from tkMessageBox import askyesno,showwarning
import os
from random import random
from string import replace
from time import time

class main:

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
        fd=open('imp.txt','r')
        app=fd.readlines()
    except:
        n=4
        font=50
    else:
        fd.close()
        n=int(replace(app[0],'\n',''))
        font=int(replace(app[1],'\n',''))
    if n==4:
        dadi=dadi4
    else:
        dadi=dadi5
    sw_salva=0

    def __init__(self):
        self.fin=Tkinter.Tk()
        self.fin.title('Paroliere')
        menu=Tkinter.Menu(self.fin)
        self.fin.config(menu=menu)
        menu.add_command(label='Help',command=self.help)
        self.fr=Tkinter.Frame(self.fin)
        self.fr.grid()
        self.crea_lb()
        self.sv_time=Tkinter.StringVar()
        self.sv_time.set('0')
        Tkinter.Label(self.fin,textvariable=self.sv_time).grid(row=1)
        self.nuovo(0)
        self.fin.bind('<F2>',self.nuovo)
        self.fin.bind('<F3>',self.cambia)
        self.fin.bind('<a>',self.ch_font)
        self.fin.bind('<z>',self.ch_font)
        #self.fin.bind('<Esc>',self.salva)
        self.fin.protocol("WM_DELETE_WINDOW",self.salva)        
        self.fin.mainloop()

    def crea_lb(self):
        self.lb=[]
        for x in range(0,self.n):
            for y in range(0,self.n):
                self.lb.append(Tkinter.Label(self.fr,font=('',self.font),bg='white',relief='sunken',borderwidth=1,text='A'))
                self.lb[-1].grid(row=x,column=y,sticky='nswe')

    def estrai_lettere(self):
        self.lettere=[]
        for x in self.dadi:
            self.lettere.append(x[int(random()*6.0)])

    def estrai_posizione(self):
        for x in range(self.n*self.n-1,-1,-1):
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
        

    def cambia(self,ev):
        self.sw_salva=1
        for x in self.lb:
            x.destroy()
        if self.n==4:
            self.n=5
            self.dadi=self.dadi5
        else:
            self.n=4
            self.dadi=self.dadi4
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

    def salva(self):
        if self.sw_salva:
            if askyesno('Salva','vuoi salvare le ultime impostazioni?'):
                fd=open('imp.txt','w')
                fd.write('%d\n%d\n'%(self.n,self.font))
                fd.close()
        self.fin.destroy()

    def help(self):
        showwarning('Help',"""Premi F2 per una nuova partita
Premi F3 per cambiare modalita' di gioco
Premi "a" oppure "z" per modificare la dimensione del carattere

Utilizza gratuitamente questo programma...
e magari fai anche tu qualcosa di
gratuito e utile per gli altri

Autore: Federico Visconti""")
            

####main###
if __name__=='__main__':
    App=main()
