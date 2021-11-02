# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 11:48:30 2021

@author: emn-0
"""

#les tekstfil
fil=open("oving_1_rein_tekst.txt")
ordliste=dict()


#registrere ordet og linjenummeret der ordet først forekommer i et dictionary
def finn_ord(linje):
    linjenummer=0
    for line in fil:
        linjenummer=linjenummer+1
        line=line.strip()
        line=line.strip("\t")
        ordene=line.split(" ")
        
        for ordet in ordene:
            if ordet not in ordliste:
                ordliste[ordet]=linjenummer
            
            
        

finn_ord(fil)
print(ordliste)





