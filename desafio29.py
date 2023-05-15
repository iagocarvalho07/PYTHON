"""
Exercício Python 29: Escreva um programa que leia a velocidade
de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem 
dizendo que ele foi multado. 
A multa vai custar R$7,00 por cada Km acima do limite.

"""
VCarro = int(input("Qual a velocidade do carro? "))
multa = (VCarro - 80)*7
if VCarro <= 80:
    print("O veiculo esta dentro do limite de velocidade da via")
else:
    print('MULTADO! vc excedeu o milite permitido que é de 80KM/h')
    print("Voçe deve pagar uma multa de R${}".format(multa))
print('tenha um bom dia! Dirija com segurança!')
