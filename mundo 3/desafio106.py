"""
Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. 
O usuário vai digitar o comando e o manual vai aparecer. 
Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará.
"""

def ajuda(comando):
    help(comando)

comando =""
while True:
    comando = input("Digite um comando ou 'FIM' para sair: ")
    if comando.upper() == 'FIM':
        print("Encerrando o programa...")
        break
    else:
        ajuda(comando)
