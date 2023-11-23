class Entrada :  
    def __init__(self, numeroDaPagina, bitDePresenca, bitDeModificacao):
        self.numeroDaPagina = numeroDaPagina
        self.bitDePresenca = bitDePresenca
        self.bitDeModificacao = bitDeModificacao

class Pagina :
    def __init__(self, enderecoLogico, processoAssociado, numeroDaPagina, bitDePresenca, bitDeModificacao):
        self.enderecoLogico = enderecoLogico
        self.processoAssociado = processoAssociado
        self.entrada = Entrada(numeroDaPagina, bitDePresenca, bitDeModificacao)
