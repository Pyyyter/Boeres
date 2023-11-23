from pagina import Pagina

def quantidadeDePaginas(tamanhoDoProcesso, tamanhoDoQuadro):
    return (tamanhoDoProcesso / tamanhoDoQuadro)

def atualizarLRU(memoriaPrincipal):
    for processo in gerenciador.tabelaDeProcessos:
        processo.contadorLRU += 1

def removerProcessoDaMemoriaPrincipalLRU(gerenciador):
    #verificar o processo com maior contadorLRU
    processo = gerenciador.tabelaDeProcessos[0]
    for processo in gerenciador.tabelaDeProcessos:
        if processo.contadorLRU > processo.contadorLRU:
            processo = processo

    #remover o processo da memoria principal
    gerenciador.tabelaDeProcessos.processos.pop(processo)
    for quadro in gerenciador.memoriaPrincipal.quadros:
        if quadro.pagina.processoAssociado == processo:
            quadro.liberarQuadro()
    gerenciador.memoriaSecundaria.processosSuspensos.append(processo)

def instrucaoDeIO(entrada):
    # Parse the input
    entrada = entrada.split(" ")
    processoID = int(entrada[2])
    dispositivoID = int(entrada[3])
    tempo = int(entrada[4])

def lerEntrada(entrada, gerenciador):
    entrada = entrada.split(" ")
    match entrada[1]:
        case "C":
            criarProcesso(entrada)
        case "I":  
            instrucaoDeIO(entrada)
        case "P":
            executarInstrucao(entrada)
        case "W":  
            escrita(entrada)
        case "R":
            leitura(entrada)
        case "T":
            terminacao(entrada)
        case _:
            print("Entrada inválida")
            return
    gerenciador.atualizarLRU()



def processoCabeNaMemoriaPrincipal(processo, memoriaPrincipal):
    quadrosLivres = 0
    for quadro in memoriaPrincipal.quadros:
        if quadro.pagina == None:
            quadrosLivres += 1

    if processo.quantidadeDePaginas >= quadrosLivres:
        return True
    else:
        return False

def colocarProcessoNaMemoriaPrincipal(self, quadros, processo):
    cabe = processoCabeNaMemoriaPrincipal(processo, self.memoriaPrincipal)
    if cabe :
        numeroDaPagina = 0
        for quadro in quadros:
            if quadro.pagina == None:
                quadro.pagina = Pagina(enderecoLogico, processo, numeroDaPagina, 1, 0)
                numeroDaPagina += 1
    else:
        self.swapper.colocarProcessoNaMemoriaPrincipal(self.memoriaPrincipal, processo)
