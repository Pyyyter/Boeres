from memorias import MemoriaPrincipal
from memorias import MemoriaSecundaria
from pagina import Pagina
from swapper import Swapper
from tools import quantidadeDePaginas
from tools import atualizarLRU
from processo import Processo
from tools import processoCabeNaMemoriaPrincipal
from tools import colocarProcessoNaMemoriaPrincipal

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
        self.filaDoPronto = []

    #Entrada é uma linha do arquivo de entrada/input
    def criarProcesso(self, entrada):
        entrada = entrada.split(" ")
        tamanhoDoProcesso = int(entrada[2])
        novoProcesso = Processo(entrada[0],tamanhoDoProcesso, self.tamanhoDaMemoriaPrincipal, self.tamanhoDoQuadro)
        self.tabelaDeProcessos.append(novoProcesso)
        self.filaDoPronto.append(novoProcesso)
        #colocarProcessoNaMemoriaPrincipal(self.memoriaPrincipal.quadros, novoProcesso)

    def mostrar_processos(self):
        for processo in self.tabelaDeProcessos:
            if processo != None:
                print(processo.nomeDoProcesso, processo.estado)