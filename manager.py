from memorias import MemoriaPrincipal
from memorias import MemoriaSecundaria
from pagina import Pagina
from swapper import Swapper
from tools import quantidadeDePaginas
from tools import atualizarLRU
from processo import Processo
from tools import processoCabeNaMemoriaPrincipal
from tools import colocarProcessoNaMemoriaPrincipal
import math

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
        self.swapper = Swapper(self)
        self.filaDoPronto = []

    #Entrada é uma linha do arquivo de entrada/input
    def criarProcesso(self, entrada):
        novoProcesso = Processo("ValorDoProcesso",entrada[0], entrada[2], self.tamanhoDoQuadro, "NOVO")
        self.tabelaDeProcessos.append(novoProcesso)
        self.filaDoPronto.append(novoProcesso)
        colocarProcessoNaMemoriaPrincipal(self, novoProcesso)

    def mostrarProcessos(self):
        for processo in self.tabelaDeProcessos:
            if processo != None:
                print(processo.nomeDoProcesso, " : ", processo.estado)

    def removerProcessoDaCpu(self):

        for i in self.tabelaDeProcessos:
            if i.estado == "executando":
                i.estado = "pronto"
                break



    def executarInstrucao(self, entrada, quadros):
        processoAtual = None
        
        for processo in self.tabelaDeProcessos:
            if processo.nomeDoProcesso == entrada[0]:
                processoAtual = processo

        self.removerProcessoDaCpu()
        
        colocarProcessoNaMemoriaPrincipal(quadros, processo)
        processo.estado = "executando"

        bitsOffset = math.log(self.tamanhoDoQuadro, 2)
        bitsEndLog = len(entrada[2])
        bitsPagina = bitsEndLog - bitsOffset

        endereco_logico = entrada[2]

        numeroDaPagina = endereco_logico[:bitsPagina]
        offset = endereco_logico[bitsPagina:bitsOffset]

        numeroDoQuadro = processo.pagina.entrada.numeroDoQuadro

        # enderecoFisico = str(numeroDoQuadro) + str(offset)

    def removerProcessoDaTabela(self, processo):
        for i in range(len(self.tabelaDeProcessos) - 1):
            if self.tabelaDeProcessos[i].nomeDoProcesso == processo:
                self.tabelaDeProcessos.pop(i)

    def terminacao(self, nomeDoProcesso):
        for quadro in self.memoriaPrincipal.quadros:
            if quadro.pagina and quadro.pagina.processoAssociado.nomeDoProcesso == nomeDoProcesso:
                quadro.liberarQuadro()

        for p in self.memoriaSecundaria.processosSuspensos:
            if p.nomeDoProcesso == nomeDoProcesso:
                self.memoriaSecundaria.processosSuspensos.remove(p)

        self.removerProcessoDaTabela(nomeDoProcesso)


    def realizarLeitura(self, nomeProcesso, endereco):

        bitsOffset = math.log(self.tamanhoDoQuadro, 2)
        bitsEndLog = len(entrada[1])
        bitsPagina = bitsEndLog - bitsOffset
        
        processo = None

        for i in self.tabelaDeProcessos:
            if i.nomeDoProcesso == nomeProcesso:
                processo = i
                
        if processo is None: 
            return        
        

        if numero_pagina < processo.quantidadeDePaginas:
            pagina = processo.tabelaDePaginas[numero_pagina]
            if pagina.entrada.bitDePresente == 1:
                print(f"Leitura do endereço {endereco} no processo {processo.nomeDoProcesso}: Valor {pagina.dados[offset]}")
                processo.contadorLRU = 0
            else:
                print(f"Falha na leitura: Página não está na memória principal.")
        else:
            print(f"Falha na leitura: Endereço {endereco} fora do espaço de endereçamento do processo.")

    def realizarEscrita(self, processo, endereco, dados):
        numero_pagina = endereco[:5]
        offset = endereco[7:]

        if numero_pagina < processo.quantidadeDePaginas:
            pagina = processo.tabelaDePaginas[numero_pagina]
            if pagina.entrada.bitDePresente == 1:
                pagina.dados[offset] = dados
                print(f"Escrita do valor {dados} no endereço {endereco} no processo {processo.nomeDoProcesso}.")
                processo.contadorLRU = 0
            else:
                print(f"Falha na escrita: Página não está na memória principal.")
        else:
            print(f"Falha na escrita: Endereço {endereco} fora do espaço de endereçamento do processo.")

    # def executarInstrucao(entrada):
    #     if()