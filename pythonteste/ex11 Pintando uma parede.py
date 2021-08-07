a1 = float(input('Digite a altura da parede: '))
l1 = float(input('Digite a largura da parede: '))
area = a1 * l1
print("Sua perede tem {:.2f} x {:.2f} e sua área é de {:.2f} m²".format(a1, l1, area))
tinta = 2
qtd_tinta = area / tinta

print('A quantidade de tinta necessária é {} litros de tinta '.format(qtd_tinta))