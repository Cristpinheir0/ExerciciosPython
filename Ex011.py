altura = float(input('Digite a altura da parede:'))
largura = float(input('Digite a largura da parede:'))
a = altura * largura

print('Para você pintar a parede de {}m^2 serão necessários {}L de tinta'.format(a, a/2))
