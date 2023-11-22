class Quadro :
    def __init__(self):
        self.pagina = None
    def liberarQuadro(self):
        self.pagina = None

class MemoriaPrincipal :
    def __init__(self, tamanhoDoQuadro, tamanhoDaMemoriaPrincipal):
        self.quadros = []
        for i in range(tamanhoDaMemoriaPrincipal / tamanhoDoQuadro):
            self.quadros.append(Quadro())

class MemoriaSecundaria :
    def __init__(self, tamanhoDaMemoria):
        self.tamanhoDaMemoria = tamanhoDaMemoria
        self.processosSuspensos = []
