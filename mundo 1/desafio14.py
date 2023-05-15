print(' a cada dia alugado e devido o valor de 60R$ e soma-se a isso 0,15 Centavos para cada km rodado')
DiasAlugados = int(input('quantos dias o carro ficou alugado? '))
TotalDeKmRodado = float(input('quantos KM foram rodados no total des do dia de inicio do aluguel até a entrega do carro? '))
TotalAPagar = (DiasAlugados*60)+(TotalDeKmRodado*0.15)

print(' o veiculo foi alugado por {} dias e rodou {}kms, deste modo é devido um valor de {}'.format(DiasAlugados, TotalDeKmRodado, TotalAPagar))

