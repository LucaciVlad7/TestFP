from business.service_pariuri import ServicePariuri
from infrastructura.repo_pariuri import RepoPariuri
from domeniu.id_si_cine_castiga import IdPlusCastig

class Teste(object):
    def __init__(self):
        self.repo = RepoPariuri("infrastructura/meciuri")
        self.service = ServicePariuri(self.repo)

    def ruleaza_toate_testele(self):
        lista=self.repo.lista_pariuri_functie()
        assert len(lista) == 4
        assert lista[0].echipa_acasa=="Steaua"

        pariu_cautat=self.repo.findByNr(1)
        assert pariu_cautat.echipa_acasa=="Steaua"

        #service 1
        lista=self.service.vizualizare_cota(1.6)
        assert len(lista) == 1
        assert lista[0].echipa_acasa=="Rapid"
        assert lista[0].cota_victorie==1.6

        #service 2

        ob=IdPlusCastig(1,1)
        lista=[]
        lista.append(ob)
        ob = IdPlusCastig(2, 1)
        lista.append(ob)
        ob = IdPlusCastig(3, 2)
        lista.append(ob)
        bilet=self.service.bilet(100,lista)
        assert bilet.suma==1344.0

        print("merge")