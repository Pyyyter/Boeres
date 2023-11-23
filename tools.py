from pagina import Pagina
# from manager import executarInstrucao 
import math
from random import randint

def quantidadeDePaginas(tamanhoDoProcesso, tamanhoDoQuadro):
    return (int(tamanhoDoProcesso) / int(tamanhoDoQuadro))

def removeN(variavel):
    for letra in variavel:
        if (letra == "\\") or (letra=="n"):
            variavel.pop(letra)

def atualizarLRU(gerenciador):
    for processo in gerenciador.tabelaDeProcessos:
        processo.contadorLRU += 1

def removerProcessoDaMemoriaPrincipalLRU(gerenciador):
    processo = gerenciador.tabelaDeProcessos[0]
    for processo in gerenciador.tabelaDeProcessos:
        if processo.contadorLRU > processo.contadorLRU:
            processo = processo

    #remover o processo da memoria principal
    removerProcessoDaMemoriaPrincipal(gerenciador, processo)

def instrucaoDeIO(entrada):
    # Parse the input
    entrada = entrada.split(" ")
    processoID = int(entrada[2])
    dispositivoID = int(entrada[3])
    tempo = int(entrada[4])

def lerEntrada(entrada, manager):
    entrada = entrada.split(" ")
    entrada[-1] = entrada[-1].replace("\n", "")
    match entrada[1]:
        case "C":
            manager.criarProcesso(entrada)
        case "I":  
            instrucaoDeIO(entrada)
        case "P":
            executarInstrucao(entrada)
        case "W":  
            print(entrada)
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
        print("Cabe")
        return True
    else:
        print("Não cabe")
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

def removerProcessoDaMemoriaPrincipal(manager, processo):
    manager.memoriaSecundaria.processosSuspensos.append(processo)
    for quadro in manager.memoriaPrincipal.quadros:
        if quadro.pagina:
            print(quadro.pagina.processoAssociado.nomeDoProcesso)
            print("Processo : ",processo.nomeDoProcesso)
            if quadro.pagina.processoAssociado.nomeDoProcesso == processo.nomeDoProcesso:
                print("liberou")
                quadro.liberarQuadro()

def colocarProcessoNaMemoriaSecundaria(memoriaSecundaria, processo):
    memoriaUsada = 0
    for processoSuspenso in memoriaSecundaria.processosSuspensos:
        memoriaUsada += processoSuspenso.tamanhoDoProcesso
    
    if(memoriaUsada + processo.tamanhoDoProcesso <= memoriaSecundaria.tamanhoDaMemoria):
        memoriaSecundaria.processoSuspensos.append(processo)
    else:
        aleatorio = randint(0, len(memoriaSecundaria.processosSuspensos))
        memoriaSecundaria.processosSuspensos.pop(aleatorio)
        colocarProcessoNaMemoriaPrincipal(memoriaSecundaria, processo)