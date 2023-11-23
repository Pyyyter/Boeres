class Entrada :  
    def __init__(self, numeroDaPagina, bitDePresenca, bitDeModificacao, numeroDoQuadro):
        self.numeroDoQuadro = numeroDoQuadro
        self.numeroDaPagina = numeroDaPagina
        self.bitDePresenca = bitDePresenca
        self.bitDeModificacao = bitDeModificacao

class Pagina :
    def __init__(self, enderecoLogico, processoAssociado, numeroDaPagina, bitDePresenca, bitDeModificacao, numeroDoQuadro):
        self.enderecoLogico = enderecoLogico
        self.processoAssociado = processoAssociado
        self.entrada = Entrada(numeroDaPagina, bitDePresenca, bitDeModificacao, numeroDoQuadro)
