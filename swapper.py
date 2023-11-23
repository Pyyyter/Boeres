from tools import processoCabeNaMemoriaPrincipal
from tools import removerProcessoDaMemoriaPrincipalLRU
from tools import colocarProcessoNaMemoriaPrincipal
from random import randint

class Swapper :
    def __init__(self, manager):
        self.manager = manager

    def colocarProcessoNaMemoriaPrincipalSwapper(self, processo):
        cabe = processoCabeNaMemoriaPrincipal(self.manager.memoriaPrincipal, processo)
        if cabe:
            colocarProcessoNaMemoriaPrincipal(self.manager.memoriaPrincipal, processo)
        while not cabe:
            removerProcessoDaMemoriaPrincipalLRU(self.manager)
            cabe = processoCabeNaMemoriaPrincipal(self.manager.memoriaPrincipal, processo)
        processo.estado = "Pronto"
        colocarProcessoNaMemoriaPrincipal(self.manager, processo)

    
    def removerProcessoDaMemoriaPrincipal(self, processo):
        memoriaUsada = 0
        for processoSuspenso in self.manager.memoriaSecundaria.processosSuspensos:
            memoriaUsada += processoSuspenso.tamanhoDoProcesso
        
        if(int(memoriaUsada) + int(processo.tamanhoDoProcesso) <= self.manager.memoriaSecundaria.tamanhoDaMemoria):
            self.manager.memoriaSecundaria.processosSuspensos.append(processo)
        else:
            aleatorio = randint(0, len(self.manager.memoriaSecundaria.processosSuspensos))
            self.manager.memoriaSecundaria.processosSuspensos.pop(aleatorio)
            self.manager.memoriaSecundaria.processosSuspensos.append(processo)
        for quadro in self.manager.memoriaPrincipal.quadros:
            if quadro.pagina:
                print(quadro.pagina.processoAssociado.nomeDoProcesso)
                print("Processo : ",processo.nomeDoProcesso)
                if quadro.pagina.processoAssociado.nomeDoProcesso == processo.nomeDoProcesso:
                    print("liberou")
                    quadro.liberarQuadro()
1