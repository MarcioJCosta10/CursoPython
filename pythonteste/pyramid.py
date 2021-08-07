empty_char = "_"
block = "#"

pyramid_length = input("Digite o tamanho da pirâmide: ")
pyramid_length = int(pyramid_length)
print(pyramid_length)

block_length = 0
rotate = 1

for x in range(pyramid_length):
	for y in range(pyramid_length - block_length):
        print(empty_char, end = '')
        print("\n")

        block_length += 1


