from os import system
import random
def SafeInput(flag):
    while 1:
        try:
            num = int(input())
            if flag == 1:
                if num > 0:
                    break
                else:
                    print("Ви помилилися. Спробуйте знову.")
                    continue
            else:
                if num > -1 and num < 2:
                    break
                else:
                    print("Ви помилилися. Спробуйте знову.")
                    continue
        except ValueError:
            print("Ви помилилися. Спробуйте знову.")
    return num
def GenerateAdjacencyMatrix():
    print("Введiть розмiрнiсть матрицi:", end = ' ')
    n = SafeInput(1)
    matrix = [[],[]]
    i = 0
    choice = input("Автоматична чи ручна генерацiя?(натиснiть 'y' для автоматичної) ")
    flag = 1
    if choice == 'y':
        flag = 0
    while i < n:
        matrix.append([])
        j = 0
        while j < n:
            if j < i:
                matrix[i].append(1 - matrix[j][i])
            else:
                if flag == 1:
                    print("Введiть елемент [%i][%i] матрицi: " % (i + 1, j + 1), end = '')
                    matrix[i].append(SafeInput(0))
                else:
                    matrix[i].append(random.randint(0, 1))
            j += 1
        i += 1
    for i in matrix:
        for j in i:
            print(j, end = ' ')
        print()
    return matrix
def CountNumberOfGraphCountours(matrix):
    bigsum = 0
    n = -2
    for i in matrix:
        n += 1
        sum = 0
        for j in i:
            sum += j
        bigsum += sum * sum
    return abs((1 / 12) * n * (n - 1) * (2 * n - 1) - bigsum / 2)
k = CountNumberOfGraphCountours(GenerateAdjacencyMatrix())
print("Кiлькiсть контурiв довжини 3: %i" %k)
system("pause")
