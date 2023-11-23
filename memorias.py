class Quadro :
    def __init__(self):
        self.pagina = None
    def liberarQuadro(self):
        self.pagina = None

class MemoriaPrincipal :
    def __init__(self, tamanhoDoQuadro, tamanhoDaMemoriaPrincipal):
        self.tamanhoDoQuadro = tamanhoDoQuadro
        self.tamanhoDaMemoriaPrincipal = tamanhoDaMemoriaPrincipal
        self.quadros = []
        for i in range(tamanhoDaMemoriaPrincipal / tamanhoDoQuadro):
            self.quadros.append(Quadro())

    def mostrar_memoria_principal(self):
        i = 0
        for quadro in self.quadros:
            if quadro == None:
                print(i, " : FREE")
            else:
                print(i," : ", quadro.pagina.processo.nomeDoProcesso)
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

                