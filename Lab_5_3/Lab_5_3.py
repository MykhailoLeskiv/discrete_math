from os import system
file = 'Roma.txt'
def CountGraphHeight(arr):
	h = 0
	for i in arr:
		if i[0] == 1: h += 1
	return h
def Passover(A, vertex, k = 1, mux = 0):
	global flow
	for i in A:
		if i[0] == vertex and i[2] != 0:
			if k == 1:
				flow.append(i[2])
				i[2] -= mux
				j = 1
				Passover(A, i[1], j, mux)
				return
			else: k -= 1
	if vertex != A[-1][0] + 1:
		flow = []
	return
def Passover2(A, vertex, k = 1, mux = 0):
	global flow
	for i in A:
##		if i[0] == vertex and i[2] != 0:
##			print(vertex)
##			if k == 1:
##				flow.append(i[2])
##				i[2] -= mux
##				j = 1
##				Passover2(A, i[1], j, mux)
##				return
##			else: k -= 1
		if i[1] == vertex and i[2] != 0:
			if k == 1:
				flow.append(i[2])
				i[2] += mux
				j = 1
				Passover2(A, i[1], j, mux)
				return
			else: k -= 1
	if vertex != A[-1][0] + 1:
		flow = []
	return
def IsBallance(A):
	i = 1
	while i <= A[-1][0] + 1:
		sum = 0
		for j in A:
			if j[0] == i:
				sum += j[2]
			elif j[1] == i:
				sum -= j[2]
		print("Рiзниця кiлькостi заходячих i виходячих потокiв вершини %i: %i" %(i, sum))
		i += 1
	return
arr = []
f = open(file)
for line in f.readlines():
    arr.append([int(item) for item in line.split()])
f.close()

maxflow = 0
while 1:
	flag = 0
	for i in range(CountGraphHeight(arr)):
		flow = []
		Passover(arr, 1, i + 1)
		if flow == []:
			flag += 1
			continue
		Passover(arr, 1, i + 1, min(flow))
		maxflow += min(flow)
	if flag == 2: break
while 1:
	flag = True
	flow = []
	Passover2(arr, 1, i + 1)
	if flow == []:
		flag = False
		break
	Passover2(arr, 1, i + 1, min(flow))
	maxflow += min(flow)
	if flag == False: break
print("Максимальний потiк заданого графа: %i" %maxflow)

for i in arr: print(i)
arr2 = []
f = open(file)
for line in f.readlines():
    arr2.append([int(item) for item in line.split()])
f.close()
for i, erow in enumerate(arr2):
	erow[2] -= arr[i][2]
print("Перевiрка умови рiвноваги: ")
IsBallance(arr2)
system('pause')
