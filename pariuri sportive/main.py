from business.service_pariuri import ServicePariuri
from infrastructura.repo_pariuri import RepoPariuri
from teste.teste_pariu import Teste
from interfata.ui import Consola

repo=RepoPariuri("infrastructura/meciuri")
service=ServicePariuri(repo)
teste=Teste()
teste.ruleaza_toate_testele()
consola=Consola(service)
consola.run()