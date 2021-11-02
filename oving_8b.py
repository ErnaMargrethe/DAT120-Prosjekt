# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 17:32:50 2021

@author: emn-0
"""

#klasse for flervalgsspørsmål



class Flervalgssporsmaal():
        
    def __init__(self, sporsmaalstekst, svaralternativer):
        self.sporsmaal=sporsmaalstekst
        self.alternativer=svaralternativer
 
        self.korrekt_svar=self.sjekk_svar()
        
        
    def __str__(self):
        return(self.__sporsmaal__(), self.svaralternativer())
        
    
        
    def sjekk_svar(self):
        self.svar=int(input("Skriv inn riktig svaralternativ her: "))
        if self.svar==1:
            print("Du har svart riktig")
        else:
                    print("Du har svart feil")
                
    
    
    
if __name__=="__main__":
    svaralternativer=list()
    svaralternativer.append("Alternativ 1: ja")
    svaralternativer.append("Alternativ 2:nei ")
    svaralternativer.append("Alternativ 3: vet ikke")
    
                    
Flervalgssporsmaal("har du bil?", svaralternativer)

#"1: ja, 2: nei, 3: vet ikke"


#spørsmålstekst, liste med svaralternativer, tall som sier hvilket alternativ som er rett

#en __str__ metode som returnerer en streng som inneholder spørsmålsteksten og nummererte svaralternativer

#sjekk_svar metode som tar parameter som heltall som representerer hvilket alternativ brukeren velger.
#skal sjekke om brukeren har lagd rett svar

#2 instanser for klassen flervalgsspørsmål, stiller spørsmålene, kommer med svaralternativene, 
#sjekker om brukeren har valgt rett svar
