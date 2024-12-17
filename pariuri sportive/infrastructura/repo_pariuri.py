from domeniu.domeniu_pariuri import Pariu
from exceptii.erori import RepoError

class RepoPariuri:
    def __init__(self, cale_fisier):
        self.__cale_fisier = cale_fisier
        self.lista_pariuri = []
        self.__citeste_tot_din_fisier()

    def lista_pariuri_functie(self):
        """
        Returneaza lista cu meciuri
        """
        return self.lista_pariuri

    def findByNr(self,number):
        #pariu_cautat=None
        #for pariu in self.lista_pariuri:
         #   if pariu.nr==number:
          #      pariu_cautat=pariu
        #if pariu_cautat==None:
        #    raise RepoError("Nu exista pariul in lista")
        #return pariu_cautat
        """
        introduci id iti returneaza meciul cu id-ul resspectiv
        :param number: id-ul dorit
        """
        if number > len(self.lista_pariuri):
            raise RepoError("Nu exista pariul in lista")
        return self.lista_pariuri[number-1]

    def __citeste_tot_din_fisier(self):
        """
        citeste din fisier si adauga in lista
        """
        with open(self.__cale_fisier,"r") as f:
            self.lista_pariuri.clear()
            linii=f.readlines()
            for linie in linii:
                linie.strip()
                if linie!="":
                    parts=linie.split(",")
                    nr=int(parts[0])
                    echipa1=parts[1]
                    echipa2=parts[2]
                    cotaV=float(parts[3])
                    cotaI=float(parts[4])
                    p=Pariu(nr,echipa1,echipa2,cotaV,cotaI)
                    self.lista_pariuri.append(p)
