from time import sleep
import random
pcnun = random.randint(0,5)
print('vou pensanr em um numero entre 0 a 5, tente adivinhar')
nun = int(input('em que numero eu pensei? '))

print('PROCESSANDO....')
sleep(3)

if nun == pcnun:
    print('vc acertou parabens')
else:
    print('numero errado eu pensei em {}'.format(pcnun)) 
