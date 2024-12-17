from exceptii.erori import RepoError
from domeniu.id_si_cine_castiga import IdPlusCastig

class Consola:
    def __init__(self,service):
        self.__service=service
        self.__comenzi={
            "1":self.__ui_vizualizare_cota,
            "2":self.__ui_creare_bilet,
        }

    def __ui_vizualizare_cota(self):
        """
        Introduci cota si iti afiseaza biletele cu cota respectiva
        """
        cota=float(input("Cota dorita: "))
        lista=self.__service.vizualizare_cota(cota)
        for element in lista:
            print(element.nr)
            print(element.echipa_acasa)
            print(element.echipa_deplasare)
            print(element.cota_victorie)
            print(element.cota_infrangere)

    def __ui_creare_bilet(self):
        """
        introduci suma si lista cu meciuri si care echipa castiga si iti returneaza
        un obiect care contine posibilul castig si lista cu id si castiguri
        :param suma: suma pariata
        :param lista_ob_pariu: lista cu meciuri si care echipa castiga
        :return: Posibilul castig(il afiseaza)
        """
        nr=int(input("Introduceti numarul de meciuri: "))
        lista_id_castig=[]
        for i in range(nr):
            id_meci=int(input("Introduceti id-ul meciului: "))
            while True:
                castiga=int(input("Introduceti 1 sau 2(primul sau al doilea meci): "))
                if castiga==1 or castiga==2:
                    break
                else:
                    print("1 sau 2 am zis")
            bilet=IdPlusCastig(id_meci,castiga)
            lista_id_castig.append(bilet)
        suma=int(input("Introduceti suma: "))
        bilet_rezultat=self.__service.bilet(suma,lista_id_castig)
        print(bilet_rezultat.suma)


    def run(self):
        """
        Functia pentru meniu de tip consola
        """
        while True:
            nume_comanda=input(">>>")
            nume_comanda.lower()
            nume_comanda.strip()
            if nume_comanda=="exit":
                break
            if nume_comanda=="":
                continue
            try:
                if nume_comanda in self.__comenzi:
                    self.__comenzi[nume_comanda]()
                else:
                    print("Nu exista comanda")
            except RepoError as re:
                print(f"Eroare de Repo: {re}")