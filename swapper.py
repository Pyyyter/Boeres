from tools import processoCabeNaMemoriaPrincipal
from tools import removerProcessoDaMemoriaPrincipalLRU
from tools import colocarProcessoNaMemoriaPrincipal
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
        colocarProcessoNaMemoriaPrincipal(self.manager.memoriaPrincipal, processo)

    def colocarProcessoNaMemoriaSecundaria():
        # verificar se na memoria tem espaco pro processo
        # se tiver, colocar o processo na memoria secundaria
        # se nao tiver espaco, remover processo da memoria secundaria aleatoriamente
        # faça isso ate caber
        # coloque o processo na memoria
        pass

