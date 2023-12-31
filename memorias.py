class Quadro :
    def __init__(self, i):
        self.pagina = None
        self.numero = i
    def liberarQuadro(self):
        self.pagina = None

class MemoriaPrincipal :
    def __init__(self, tamanhoDoQuadro, tamanhoDaMemoriaPrincipal):
        self.tamanhoDoQuadro = tamanhoDoQuadro
        self.tamanhoDaMemoriaPrincipal = tamanhoDaMemoriaPrincipal
        self.quadros = []
        for i in range(int(tamanhoDaMemoriaPrincipal / tamanhoDoQuadro)):
            self.quadros.append(Quadro(i))

    def mostrarMemoriaPrincipal(self):
        i = 0
        for quadro in self.quadros:
            if quadro.pagina == None:
                print(i, " : FREE")
            else:
                print(i," : ", quadro.pagina.processoAssociado.nomeDoProcesso)
            i+= 1
    
    def mostrarTabelasDePaginas(self):
        for quadro in self.quadros:
            if(quadro.pagina != None):
                print("Número da pagina: ", quadro.pagina.numeroDaPagina)
                print("Entrada: ")
                print("Número do quadro: ", quadro.pagina.entrada.numeroDoQuadro)
                print("B: ", quadro.pagina.bitDePresenca)
                print("M: ", quadro.pagina.bitDeModificacao)

class MemoriaSecundaria :
    def __init__(self, tamanhoDaMemoria):
        self.tamanhoDaMemoria = tamanhoDaMemoria
        self.processosSuspensos = []

    def mostrarMemoriaSecundaria(self):
        memoriaLivre = int(self.tamanhoDaMemoria)
        print("Processos suspensos : ")
        for processo in self.processosSuspensos:
            print(processo.nomeDoProcesso)
            memoriaLivre -= int(processo.tamanhoDoProcesso)
        print("Memória livre : ", memoriaLivre)
