##Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('digite uma frase: ')).lower().strip()
print('a letra A aparece {} vezes na frase '.format(frase.count('a')))
print('e ele aparece primeiro na posição {}'.format(frase.find('a')+1))
print('e ele aparece pela ultima vez na posição {}'.format(frase.rfind('a')+1))