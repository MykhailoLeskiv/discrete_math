from os import system
def IsNumber(num):
    try:
        if num[0] == '-':
            a = num[1:]
        else: a = num
    except IndexError:
        return True
    #if isinstance(a, int) == False: return False
    if a.isdigit() == False: return False
    return True

def StringGoing(str):
    comment = ''
    i, j = 0, 0
    print(str[j:i])
    while i < len(str):
        if str[i] == '{':
            if IsNumber(str[j:i]) == False and IsNumber(str[j:i]) != "":
                print(1)
                return False
            i += 1
            while str[i] != '}':
                if i == len(str) - 1:
                    print(2)
                    return False
                i += 1
##            if str[i] == '}' and str[i - 1] != '}':
##                print(3)
##                return False
            j = i + 1
        elif i == len(str) - 1:
            if IsNumber(str[j:i + 1]) == False:
                print(4)
                return False
        i += 1
    return True

if StringGoing(input('Введiть стрiчку: ')):
    print("Введена стрiчка генерується даною граматикою")
else: print("Введена стрiчка не генерується даною граматикою")
#system('pause')
