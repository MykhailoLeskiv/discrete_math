from os import system
import random
def SafeInput():
    while 1:
        try:
            A = input('Введiть K-список: ').split()
            j = 0
            for i in A:
                A[j] = i.replace(',',' ').split()
                j += 1
            if CorrectArrayInput(A):
                break
            else:
                print("Ви помилилися, cпробуйте знову.")
                continue
        except ValueError:
            print("Ви помилилися, спробуйте знову.")
    return A
def GrafTranspose(graph):
	i = 0
	n = len(graph)
	while i < n:
		graph.append([graph[i][1], graph[i][0]])
		i += 1
def CorrectArrayInput(array):
    for item in array:
        if int(item[0]) < 1 or int(item[1]) < 1 or len(item) != 2:
            return False
    return True
def AdjacentEdges(A, edge):
	global mas
	arr = []
	flag = False
	for i in A:
		if i[0] == edge and i[1] not in mas:
			mas.append(i[1])
			arr.append(i[1])
			flag = True
	if flag == True:
		for j in arr:
			if j == []: break
			arr.append(AdjacentEdges(A, j))
	return arr
def MaxKList(lst):
	mx = 0
	for i in lst:
		for j in i:
			if int(j) > mx: mx = int(j)
	return mx
def IsConnected(top, n):
	global mas
	for i in range(n):
		if str(i + 1) not in mas:
			return i + 1
	return 0

afuk = SafeInput()
temp = input("Зробити граф не орiєнтовним? (введiть 'y'): ")
if temp == "y": GrafTranspose(afuk)
i = 1
flag = True
while i <= MaxKList(afuk):
	mas = []
	AdjacentEdges(afuk, str(i))
	mas.append(str(i))
	topp = IsConnected(str(i), MaxKList(afuk))
	if topp != 0:
		print("Даний граф не зв'язний")
		print("Не iснує зв'язку мiж вершинами %i i %i" %(i, topp))
		flag = False
		break
	i += 1
if flag: print("Даний граф зв'язний")
system("pause")
