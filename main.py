from tools import lerEntrada
from tools import lerArquivo
from manager import GerenciadorDeMemoria
#Entrada : [ID] [FLAG] [ATRIBUTO]


def seleciona():
    print("1 - Mostrar memória")
    print("2 - Mostrar tabelas de páginas")
    print("3 - Mostrar processos e seus estados")
    print("4 - Ler entrada em arquivo")
    print("5 - Ler entrada com input")
    print("6 - Sair")
    return int(input("Digite a opção desejada: "))

    

# arquivo = open("entrada.txt", "r")
# for linha in arquivo:
#     lerEntrada(linha)

def inicio(manager):
    resposta = seleciona()
    if(resposta == 1):
      manager.memoriaPrincipal.mostrarMemoriaPrincipal()
      print("------------------------------------------")
      manager.memoriaPrincipal.mostrarMemoriaSecundaria()
    if(resposta == 2):
       manager.memoriaPrincipal.mostrarTabelasDePaginas()
    if(resposta == 3):
       manager.mostrarProcessos()
    if(resposta == 4):
       lerArquivo(input("Nome do arquivo : "), manager)
    if(resposta == 5):
       lerEntrada(input("Digite a entrada : "), manager)
    if(resposta == 6):
       print("Saindo...")
    print("------------------------------------------")
    inicio(manager)
    

def teste():
    manager = GerenciadorDeMemoria(1024, 4096, 16, 12)
    inicio(manager)
    # manager.criarProcesso("P1 1 160")
    manager.memoriaPrincipal.mostrarMemoriaPrincipal()

teste()