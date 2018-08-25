from os import system
from itertools import product
def PrintSet(Set):
	print("{", end='')
	print(','.join(Set), end='}')
	return ''
def PrintCartesianProduct(Set1, Set2):
	Product = [Set1, Set2]
	Product = list(product(*Product))
	print("{", end='')
	for i in Product:
		print("(" + i[0] + "," + i[1] + ")", end='')
		if i != Product[-1]:
			print(";", end='')
	print("}")
	del Product
	return
def ReadSetElement(string, index):
	a = []
	while string[index] != "," and string[index] != "}":
		a.append(string[index])
		if index < len(string):
			index = index + 1
		else:
			break
	myString = ''.join(a)
	del a
	return myString
def ReadSetIntoArray(f):
	line = f.readline()
	if (line[1] == '}'):
		return []
	array = []
	for i, symbol in enumerate(line):
		if symbol == "," or i == 0:
			if line[i + 1] != ",":
				array.append(ReadSetElement(line, i + 1))
	return array
f = open('text.txt', 'r')
A = ReadSetIntoArray(f)
B = ReadSetIntoArray(f)
f.close()
print("Масив A: ", end='')
print(PrintSet(A))
print("Масив B: ", end='')
print(PrintSet(B))
print('\nДекартiв добуток A*B:')
PrintCartesianProduct(A, B)
print('\nДекартiв добуток B*A:')
PrintCartesianProduct(B, A)
del A, B
system('pause')