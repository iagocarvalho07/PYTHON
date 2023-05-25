from moduloDesafios import mudulodesafio108
from mudulodesafio108 import ___init__

digiteUmNumero = float(input("Digite o preço do produto:R$ "))


mudulodesafio108.aumentar(digiteUmNumero)
print(f" o preço do produto mais 10% e igual a {mudulodesafio108.aumentar(digiteUmNumero)}")
print(f" o dobro do preço do produto e igual a {mudulodesafio108.dobro(digiteUmNumero)}")
print(f" o preço do produto menos 10% e igual a {mudulodesafio108.diminuir(digiteUmNumero)}")
print(f" o preço do produto pela metada e igual a {mudulodesafio108.metade(digiteUmNumero)}")

