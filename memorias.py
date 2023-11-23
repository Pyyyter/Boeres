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

class MemoriaSecundaria :
    def __init__(self, tamanhoDaMemoria):
        self.tamanhoDaMemoria = tamanhoDaMemoria
        self.processosSuspensos = []

    def mostrar_memoria_secundaria(self):
        i=0
        for processo in self.processosSuspensos:
            if processo == None:
                print(i, " : FREE")
            else:
                print(i, " : ", processo.nomeDoProcesso)



                