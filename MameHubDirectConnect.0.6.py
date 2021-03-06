#-*- coding: utf-8 -*-
#Version 0.6

def Help()  :

    ''' Script offrant un GUI minimal
    pour la connexion p2p à Csume64,émulateur utilisé par MAMEHub.

    *En mode SERVEUR (Héberger) :
    1- Cocher le bouton héberger,le champ IP de l'hôte doit rester vide.
    Votre addresse IP publique est donnée dans le shell via le site
    monip.org , c'est cette Ip qu'il faut transmettre au CLIENT.
    2-Choisissez un Pseudo et remplir le champ
    3-Entrer le zipname du jeu à lancer  ,pour street fighter 2 ,
    taper sf2 par exemple.

    * En mode CLIENT (Rejoindre):
    1-Cocher le bouton Rejoindre.
    2-Entrer l'adresse IP donnée par le SERVEUR.
    3-Choississsez un Pseudo et renseigner le champ.
    4-Entrer le zipname du jeu à lancer  ,pour street fighter 2 ,
    taper sf2 par exemple.

    TODO LIST:
    -Ajouter un chat pour transmettre l'adresse IP.
    -Ajouter un lancement en mode solo? '''
import os, urllib.request, sys, re
from html.parser import HTMLParser
from tkinter import *
from tkinter.filedialog import *
print(os.name)

class Monipclean(HTMLParser):
    def handle_data(self, data):
        print(data)

if len(sys.argv)>1:
       if sys.argv[1]=='-h' or '--help' :
                print(Help.__doc__)
global deco , parsed ,binpath ,exepath ,v3
binpath=os.path.join('MAMEHubRepo','Binaries')
try : os.chdir(binpath)
except FileNotFoundError :
    print('/!\ Chemin incorrect, fermer l\'applicaton et placer le script à l\'emplacement correct')
    exit()

#os.chdir( "MAMEHubRepo\Binaries")
curent = os.getcwd()
print(curent)
url=urllib.request.urlopen("http://www.monip.org")

page=url.read()
deco=page.decode('ISO-8859-1')
parser=Monipclean()
parser.feed(deco)

fenetre=Tk()
fenetre.title('MameHub Direct Connect -By JustaLiriK-')
fenetre.geometry('550x120')
v1=StringVar()
v2=StringVar()
v3=StringVar()
r=IntVar()
def fichier():
        path=askopenfilename(title='Choisir une rom à lancer',filetypes=[('fichiers zip','.zip')])
        print(path)
        result=re.split('\W',path)
        i=len(result)-2
        piz=result[i]
        e3.insert(0,piz)


Radiobutton(fenetre,text="Héberger" ,variable=r , value=1).grid(row=0, column=0)
Radiobutton(fenetre, text="Rejoindre" ,variable=r , value=2).grid(row=0 , column=1)

e1=Entry(fenetre,textvariable=v1)
e2=Entry(fenetre,textvariable=v2)
e3=Entry(fenetre,textvariable=v3)

b3=Button(fenetre,text='Rom à lancer',command=fichier)

e1.grid(row=2,column=1)
e2.grid(row=3, column=1)
e3.grid(row=4,column=1)
b3.grid(row=4, column=0)

l1=Label(fenetre, text="IP de l'hôte à joindre (mode client uniquement): ")
l2=Label(fenetre, text="Entrez votre Pseudo ici : ")


l4=Label(fenetre, text=".zip")

l1.grid(row=2,column=0)
l2.grid(row=3,column=0)
l4.grid(row=4, column=2)



def resetall():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0,END)

def launch ():
    mode=r.get()
    player=e2.get()

    rom=e3.get()
    host=e1.get()

    if os.name=="nt":
        exepath=os.path.join('dist','csume64.exe')
    else:
        exepath=os.path.join('dist','csume64')
    try : exepath
    except FileNotFoundError :
        print('/!\ Chemin incorrect, fermer l\'applicaton et vérifier que le l\'exécutable soit présent')
        exit()
    if mode==1 :
           # execute="dist\csume64.exe " + rom +" -server -port 6805  -username "+ player
           execute=exepath +" "+ rom +" -server -port 6805  -username "+ player
    else :

          # execute="dist\csume64.exe " + rom +" -client -port 6805 -hostname " + host + " -username " + player
          execute=exepath +" "+ rom +" -client -port 6805 -hostname " + host + " -username " + player
    print("c'est parti!")
    print( execute)
    os.system(execute)

b1=Button(fenetre, text="R.A.Z.", command=resetall, cursor='exchange')
b2=Button(fenetre, text="Lancer" , command=launch, cursor='shuttle')
b1.grid(row=5, column=1)
b2.grid(row=5 , column=2)
mainloop()


