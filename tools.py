from pagina import Pagina
import math
from random import randint

def quantidadeDePaginas(tamanhoDoProcesso, tamanhoDoQuadro):
    return (int(tamanhoDoProcesso) / int(tamanhoDoQuadro))

def removeN(variavel):
    for letra in variavel:
        if (letra == "\\") or (letra=="n"):
            variavel.pop(letra)

def atualizarLRU(gerenciador):
    for quadro in gerenciador.memoriaPrincipal.quadros:
        if quadro.pagina:
            quadro.pagina.contadorLRU += 1

def removerPaginaDaMemoriaPrincipalLRU(gerenciador):

    paginaARemover = None
    for pagina in gerenciador.memoriaPrincipal.quadros:
        if pagina:
            if paginaARemover.pagina == None:
                paginaARemover = pagina
            if pagina.contadorLRU > paginaARemover.contadorLRU:
                paginaARemover = pagina     
    paginaARemover.liberarQuadro()

def instrucaoDeIO(entrada):
    # Parse the input
    entrada = entrada.split(" ")
    processoID = int(entrada[2])
    dispositivoID = int(entrada[3])
    tempo = int(entrada[4])



def lerEntrada(entrada, manager):
    atualizarLRU(manager)
    for processo in manager.tabelaDeProcessos:
        print("Processo : ", processo.nomeDoProcesso, " / ", "LRU : ", processo.contadorLRU)
    entrada = entrada.split(" ")
    entrada[-1] = entrada[-1].replace("\n", "")
    match entrada[1]:
        case "C":
            manager.criarProcesso(entrada)
        case "I":  
            manager.instrucaoDeIO(entrada)
        case "P":
            manager.executarInstrucao(entrada)
        case "W":
            manager.realizarEscrita(entrada[0], entrada[2], entrada[3])
        case "R":
            manager.realizarLeitura(entrada[0], entrada[2])
        case "T":
            manager.terminacao(entrada[0])
        case "S":
            manager.memoriaPrincipal.mostrarMemoriaPrincipal()
        case _:
            print("Entrada inválida")
            return
    atualizarLRU(manager)

def processoCabeNaMemoriaPrincipal(memoriaPrincipal, processo):
    quadrosLivres = 0
    for quadro in memoriaPrincipal.quadros:
        if quadro.pagina == None:
            quadrosLivres += 1
    if processo.quantidadeDePaginas <= quadrosLivres:
        return True
    else:
        return False

def colocarProcessoNaMemoriaPrincipal(manager, processo):
    numeroDePaginas = math.ceil(processo.quantidadeDePaginas)
    cabe = processoCabeNaMemoriaPrincipal(manager.memoriaPrincipal,processo)
    if cabe:
        numeroDaPagina = 0
        for quadro in manager.memoriaPrincipal.quadros:
            if quadro.pagina == None and numeroDePaginas > 0:
                quadro.pagina = Pagina(processo, numeroDaPagina, 1, 0 , quadro.numero)
                numeroDaPagina += 1
                numeroDePaginas -=1
        processo.estado = "PRONTO"
    else:
        manager.swapper.colocarProcessoNaMemoriaPrincipalSwapper(processo)

def lerArquivo(path, manager):
    arquivo = open(path, 'r')
    for linha in arquivo :
        lerEntrada(linha, manager)
