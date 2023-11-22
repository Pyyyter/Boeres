def quantidadeDePaginas(tamanhoDoProcesso, tamanhoDoQuadro):
    return (tamanhoDoProcesso / tamanhoDoQuadro)

def atualizarLRU(gerenciador):
    for processo in gerenciador.tabelaDeProcessos:
        processo.contadorLRU += 1

def removerProcessoDaMemoriaPrincipal(self, processo1):
    self.tabelaDeProcessos.processos.pop(processo1)
    for quadro in self.memoriaPrincipal.quadros:
        if quadro.pagina.processoAssociado == processo1:
            quadro.liberarQuadro()
    self.memoriaSecundaria.processosSuspensos.append(processo1)

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