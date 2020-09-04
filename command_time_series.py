import nltk
nltk.download('punkt')
from gtts import gTTS
import pygame.mixer
import time
import os
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import webbrowser

#Le receuille du son, etant pas facile sur tout a temps reel, essayon d'utiliser un mot a l'exemple(eteindre)
eteindre=[t,X(t)]

#Tableu des valeurs de la serie
def coordonnees(song):
    table=[]
    return table

#Table=coordonnees(Song)

#Creation/Lecture d'une expression
def sonn(my_text,t):
    language=('fr')
    fich="audio"+str(t)+".mp3"
    my_audio=gTTS(text=my_text,lang=language,slow=False)
    my_audio.save(fich)
    pygame.mixer.init()
    pygame.mixer.music.load(fich)
    pygame.mixer.music.play()
    time.sleep(6)


#Etrainement de la lecture des mots
#Cette etape ne necessite qu'une seul execution
def dict_entrainement_mots():
    f=open('/home/ams/Bureau/Serie chrono/liste_francais.txt','r')
    tex=f.read()
    mots=tex.split()
    d={}
    for i in mots:
        sonn(i,0)
        song=i+".mp3"
        mot=coordonnees(song)
        X=mot[1].interpolate(inplace=True)
        dec = sm.tsa.seasonal_decompose(X)
        #dec est constitue de 3 listes: tendence,saison,residu
        d[i]=dec
    return d

#global dict_mots_pre_entraine
dict_mots_pre_entraine=dict_entrainement_mots()

#Recevoir et subdiviser un son: 1ere etatpe

#Division en tranche

Table=eteindre

def divise_mots(table):
    lm=[]
    t=table[0]
    X=table[1]
    pos=0
    for i in range(len(t)):
        while abs(X[i])>0.001:
            i+=1
        m=(t[pos:i],X[pos:i])
        lm.append(m)
        pos=i
    return lm

list_mots=divise_mots(Table)  

#Caracterisation des mots de l'auteur: 2eme etape

def dict_caracterisation_mot(list_mots):
  
     ide=0 #identite des mot
     dict_mots={}
     for mot in list_mots:
    
         X=mot[1].interpolate(inplace=True)
         dec = sm.tsa.seasonal_decompose(X)
         #dec est constitue de 3 listes: tendence,saison,residu
         dict_mots[ide]=dec
         ide+=1 
     return dict_mots


dict_mots=dict_caracterisation_mot(list_mots)

#Reconstitution de l'expression d'auteur: 3eme etape
def reconstitu_com(dict_mots):
    command=""
    for mot in dict_mots.values():
        command+=list(dict_mots_pre_entraine.keys())[list(dict_mots_pre_entraine.values()).index(mot)]
    return command
    
Command=reconstitu_com(dict_mots)

#Ex: Command="eteindre mon odinateur!"

#Classe des executions possibles
class execution_com:

    def __init__(self):
         self.action=""
         self.nom=""

    def eteindre(self):
         my_text0="Voulez vous eteindre votre ordinateur?"
         sonn(my_text0,0)
         choice=messagebox.askyesno("Eteindre?","Voudriez vous eteindre le PC?")
         if choice==True:
            my_text1="D'accord. Veillez patienter!"
            sonn(my_text1,1)
            try:
                 os.system("shutdown")
            except: 
             my_text="Oups, une erreur s'est produite. Veiller le faire manuellement!"
         else:
            my_text2="Ah! J'allait vous dire que vous allez me manquer enormement monsieur Abdoul Madjid."
            sonn(my_text2,2)
            exit()
 
   
    def creer_dossier(self):
         my_text0="Voulez vous creer un dossier "+self.nom+"?"
         sonn(my_text0,0)
         choice=messagebox.askyesno("Creer?","Voudriez vous creer le nouveau dossier"+self.nom+"?")
         if choice==True:
            my_text1="D'accord. A votre service!"
            sonn(my_text1,1)
            act=self.action+self.nom
            try:
                os.system(act)
            except: 
                my_text="Oups, une erreur s'est produite. Veiller le faire manuellement!"
         else:
            my_text2="Ok, comme vous voudriez monsieur Abdoul Madjid."
            sonn(my_text2,2)
            exit()
 
   
        
    def ouvre_dossier(self):
         my_text0="Voulez vous ouvrir le dossier "+self.nom+"?"
         sonn(my_text0,0)
         choice=messagebox.askyesno("Voulez vous ouvrir le dossier "+self.nom+"?")
         if choice==True:
            my_text1="D'accord. A votre service!"
            sonn(my_text1,1)
            act=self.action+self.nom
            try:
                os.system(act)
            except: 
                my_text="Oups, une erreur s'est produite. Veiller le faire manuellement!"
         else:
            my_text2="Ok, comme vous voudriez monsieur Abdoul Madjid."
            sonn(my_text2,2)
            exit()
        
    def modif_dossier(self):
         my_text0="Voulez vous modifier le dossier "+self.nom+"?"
         sonn(my_text0,0)
         choice=messagebox.askyesno("Voulez vous modifier le dossier "+self.nom+"?")
         if choice==True:
            my_text1="D'accord. A votre service!"
            sonn(my_text1,1)
            act=self.action+self.nom
            try:
                os.system(act)
            except: 
                my_text="Oups, une erreur s'est produite. Veiller le faire manuellement!"
         else:
            my_text2="Ok, comme vous voudriez monsieur Abdoul Madjid."
            sonn(my_text2,2)
            exit()
        
    def suppri_fich(self):
         my_text0="Voulez vous supprimer le dossier "+self.nom+"?"
         sonn(my_text0,0)
         choice=messagebox.askyesno("Voulez vous supprimer le dossier "+self.nom+"?")
         if choice==True:
            my_text1="D'accord. A votre service!"
            sonn(my_text1,1)
            act=self.action+self.nom
            try:
                os.system(act)
            except: 
                my_text="Oups, une erreur s'est produite. Veiller le faire manuellement!"
         else:
            my_text2="Ok, comme vous voudriez monsieur Abdoul Madjid."
            sonn(my_text2,2)
            exit()
        
    def requete_web(self):
         my_text0="Voulez vous consulter la page "+self.nom+"?"
         sonn(my_text0,0)
         choice=messagebox.askyesno("Voulez vous consulter la page "+self.nom+"?")
         if choice==True:
            my_text1="D'accord. A votre service!"
            sonn(my_text1,1)
            try:
                webbrowser.open(self.nom)
            except: 
                my_text="Oups, une erreur s'est produite. Veiller le faire manuellement!"
         else:
            my_text2="Ok, comme vous voudriez monsieur Abdoul Madjid."
            sonn(my_text2,2)
            exit()
        

    def editer_text(self):
         my_text0="Voulez vous editer un fichier nomme "+self.action+"?"
         sonn(my_text0,0)
         choice=messagebox.askyesno("Voulez vous editer un fichier nomme "+self.action+"?")
         if choice==True:
            my_text1="D'accord. A votre service!"
            sonn(my_text1,1)
            try:
                fich=self.action+".txt"
                f=open(fich,'a')
                f.write(self.nom)
                f.close()
            except: 
                my_text="Oups, une erreur s'est produite. Veiller le faire manuellement!"
         else:
            my_text2="Ok, comme vous voudriez monsieur Abdoul Madjid."
            sonn(my_text2,2)
            exit()
        

    def executer(self):
         my_text0="Voulez vous Executer "+self.action+"?"
         sonn(my_text0,0)
         choice=messagebox.askyesno("Voulez vous executer "+self.action+"?")
         if choice==True:
            my_text1="D'accord. A votre service!"
            sonn(my_text1,1)
            act=self.action
            try:
                os.system(act)
            except: 
                my_text="Oups, une erreur s'est produite. Veiller le faire manuellement!"
         else:
            my_text2="Ok, comme vous voudriez monsieur Abdoul Madjid."
            sonn(my_text2,2)
            exit()
        
#Traitement de l'expression de l'auteur et execution de la commande: Etape 4
def action(Command):
    command=Command.split()
    command=set(command)
    ex=execution_com()

    eteindre={"eteindre","eteins","t'etindre","d'eteindre","eteind"}
    ouvre={"ouvre","ouvrir","ouverture"}
    executer={"executer","execute","execution"}
    supprime={"supprimer","supprime","effacer","efface"}
    recherche={"rechercher","recherche","requete","chercher","cherche"}
    creer={"creer","cree"}
    modifier={"modifier","modifie","changer","change"}
    editer={"editer","ecrire","rediger","edite","ecris","redige"}
    
    if len(command.intersection(eteindre))!=0:
         ex.eteindre()
    if len(command.intersection(ouvre))!=0:
         ex.action="nautilus "
         ex.nom="AMS2"
         ex.ouvre_dossier()
    if len(command.intersection(executer))!=0:
         ex.action="google-chrome"
         ex.executer()
    if len(command.intersection(supprime))!=0:
         ex.action="rm -r "
         ex.nom="AMS2"
         ex.suppri_fich()
    if len(command.intersection(recherche))!=0:
         ex.nom="https://www.google.com/"
         ex.requete_web()
    if len(command.intersection(creer))!=0:
         ex.action="mkdir "
         ex.nom="AMS1"
         ex.creer_dossier()
    if len(command.intersection(modifier))!=0:
         ex.action="mv "
         ex.nom="AMS1 AMS2"
         ex.modif_dossier()
    if len(command.intersection(editer))!=0:
         ex.nom="Bonjour et bienvenu!"
         ex.action="salut"
         ex.editer_text() 
     
action(Command)

try:
    os.system("rm audio0.mp3 audio1.mp3 audio2.mp3")
except:
    os.system("rm audio2.mp3")