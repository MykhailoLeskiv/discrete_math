from os import system
def SafeInput():
    while 1:
        A = input('Введiть вектор значень(булевих): ').split()
        if CorrectArrayInput(A) and len(A) & (len(A) - 1) == 0:
            break
        else:
            print("Ви помилилися, cпробуйте знову.")
            continue
    return A
def CorrectArrayInput(array):
    
    for item in array:
        if item != '0' and item != '1':
            return False
    return True
def ZhegalkinPolynom(arr):
    downarr = []
    i = 0
    if len(arr) == 1:
        return
    while i < len(arr) - 1:
        downarr.append(arr[i] != arr[i + 1])
        i += 1
    polynom.append(downarr)
    ZhegalkinPolynom(downarr)
def LinearCheck(triangle):
    arr = []
    for item in triangle:
        arr.append(item[0])
    i = int((len(arr) + 1)/2 - 2)
    while i < len(arr):
        if arr[i] == 1 and (len(arr) - i - 1) & (len(arr) - i - 2) == 0:
            return False
            break
        else:
            i += 1
    return True

polynom = []
ZhegalkinPolynom(SafeInput())
if LinearCheck(polynom): print('Дана функцiя лiнiйна')
else: print('Дана функцiя не лiнiйна')
system('pause')
