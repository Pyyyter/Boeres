from tools import quantidadeDePaginas

class Processo :
    def __init__(self, valorDoProcesso, nomeDoProcesso, tamanhoDoProcesso, tamanhoDoQuadro):
        self.valorDoProcesso = valorDoProcesso
        self.nomeDoProcesso = nomeDoProcesso
        self.tamanhoDoProcesso = tamanhoDoProcesso
        self.quantidadeDePaginas = quantidadeDePaginas(tamanhoDoProcesso, tamanhoDoQuadro)
        self.tabelaDePaginas = []
        self.contadorLRU = 0
