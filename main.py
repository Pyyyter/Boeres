
#Entrada : [ID] [FLAG] [ATRIBUTO]


def seleciona():
    print("1 - Mostrar memória")
    print("2 - Mostrar tabelas de páginas")
    print("3 - Mostrar processos e seus estados")
    print("4 - Ler entrada em arquivo")
    print("5 - Ler entrada com input")
    print("6 - Sair")
    return int(input("Digite a opção desejada: "))

arquivo = open("entrada.txt", "r")
for linha in arquivo:
    lerEntrada(linha)

def inicio():
    print("1 - ")