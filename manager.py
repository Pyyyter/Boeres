from memorias import MemoriaPrincipal
from memorias import MemoriaSecundaria
from pagina import Pagina
from swapper import Swapper
from tools import quantidadeDePaginas
from tools import atualizarLRU

class GerenciadorDeMemoria :

    def __init__(self, tamanhoDaMemoriaPrincipal, tamanhoDaMemoriaSecundaria, tamanhoDoQuadro, tamanhoEnderecoLogicoEmBits):
        self.tamanhoDaMemoriaPrincipal = tamanhoDaMemoriaPrincipal
        self.tamanhoDaMemoriaSecundaria = tamanhoDaMemoriaSecundaria
        self.tamanhoDoQuadro = tamanhoDoQuadro
        self.tamanhoEnderecoLogicoEmBits = tamanhoEnderecoLogicoEmBits
        self.tabelaDeProcessos = []
        self.numeroDeQuadros = tamanhoDaMemoriaPrincipal / tamanhoDoQuadro
        self.memoriaPrincipal = MemoriaPrincipal(tamanhoDoQuadro, tamanhoDaMemoriaPrincipal)
        self.memoriaSecundaria = MemoriaSecundaria(tamanhoDaMemoriaSecundaria)
        self.swapper = Swapper(self.memoriaPrincipal, self.memoriaSecundaria, self.tabelaDeProcessos)

    #Entrada é uma linha do arquivo de entrada/input
    def criarProcesso(self, entrada):
        entrada = entrada.split(" ")
        tamanhoDoProcesso = int(entrada[2])
        novoProcesso = Processo(entrada[0],tamanhoDoProcesso, self.tamanhoDaMemoriaPrincipal, self.tamanhoDoQuadro)
        self.tabelaDeProcessos.append(novoProcesso)        
    

    def colocarProcessoNaMemoria(self, quadros, processo):
        livres = 0

        for processo in self.tabelaDeProcessos:
            if processo != processo:
                processo.contadorLRU += 1
            
        for quadro in quadros:
            if quadro.pagina == None:
                livres += 1

        if livres >= processo.quantidadeDePaginas:
            numPagina = 0
            for quadro in quadros:
                if quadro.pagina == None:
                    quadro.pagina = Pagina(processo, numPagina, 1, 0) # Consertar o numero da pagina
                    processo.quantidadeDePaginas -= 1
                    numPagina += 1
                    return quadro
        else:
            self.swapper.substituirProcesso(quadros, processo)
            self.colocarProcessoNaMemoria(quadros, processo)
    