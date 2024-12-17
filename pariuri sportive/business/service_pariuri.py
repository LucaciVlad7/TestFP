from domeniu.bilet import Bilet

class ServicePariuri:
    def __init__(self,repo):
        self.__repo=repo

    def vizualizare_cota(self,cota):
        """
        Returneaza lista meciurilor care au una dintre cote mai mare ca cea introdusa
        :param cota: Cota dorita
        """
        lista_pariuri=self.__repo.lista_pariuri_functie()
        lista_valide=[]
        for pariu in lista_pariuri:
            if pariu.cota_victorie==cota or pariu.cota_infrangere==cota:
                lista_valide.append(pariu)
        return lista_valide

    def bilet(self,suma,lista_ob_pariu):
        """
        introduci suma si lista cu meciuri si care echipa castiga si iti returneaza
        un obiect care contine posibilul castig si lista cu id si castiguri
        :param suma: suma pariata
        :param lista_ob_pariu: lista cu meciuri si care echipa castiga
        """
        lista_pariuri = self.__repo.lista_pariuri_functie()
        cota_totala=1
        for pariu in lista_ob_pariu:
            cota_curenta=1
            if pariu.castig==1:
                cota_curenta=lista_pariuri[pariu.id_pariu-1].cota_victorie
            elif pariu.castig==2:
                cota_curenta = lista_pariuri[pariu.id_pariu-1].cota_infrangere
            cota_totala=cota_totala*cota_curenta
        suma_cota=suma*cota_totala
        bilet=Bilet(lista_ob_pariu,suma_cota)
        return bilet