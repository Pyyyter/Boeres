from tools import processoCabeNaMemoriaPrincipal
from tools import removerProcessoDaMemoriaPrincipalLRU
from tools import colocarProcessoNaMemoriaPrincipal
class Swapper :
    
    def colocarProcessoNaMemoriaPrincipalSwapper(memoriaPrincipal, processo):
        cabe = processoCabeNaMemoriaPrincipal(memoriaPrincipal, processo)
        if cabe:
            colocarProcessoNaMemoriaPrincipal(memoriaPrincipal, processo)
        while not cabe:
            removerProcessoDaMemoriaPrincipalLRU(memoriaPrincipal, processo)
            cabe = processoCabeNaMemoriaPrincipal(memoriaPrincipal, processo)
        colocarProcessoNaMemoriaPrincipal(memoriaPrincipal, processo)

    def colocarProcessoNaMemoriaSecundaria():
        # verificar se na memoria tem espaco pro processo
        # se tiver, colocar o processo na memoria secundaria
        # se nao tiver espaco, remover processo da memoria secundaria aleatoriamente
        # faça isso ate caber
        # coloque o processo na memoria
        pass

