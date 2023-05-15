largura = int(input('qual a largura da parede'))
altura = int(input('qual a altura da parede'))
comprimento = largura*altura
print('sua parede tem as dimençoes de {}x{} deste modo tem uma area total de {}m²'.format(largura, altura, comprimento ))
print('para pintar essa parede vc precisara de {} litros de tinta'.format((comprimento/2)))