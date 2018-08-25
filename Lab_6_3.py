from os import system
import re
def GenerateAlphabet():
	arr = []
	i = 42
	while i <= 122:
		arr.append(chr(i))
		if i == 43: i += 2
		elif i == 57: i += 8
		elif i == 90: i += 7
		else: i += 1
	arr[3], arr[4] = arr[4], arr[3]
	return arr
def GenerateClassArray(alp):
	arr = []
	arr.append(alp[0:4])
	arr.append(alp[5:15])
	arr.append(alp[15:67])
	return arr
def CheckString(str, alp):
	if str[0] in alp[0] or str[-1] in alp[0]: return False
	i = 0
	while i < len(str):
		if str[i] in alp[0] and str[i + 1] in alp[0]: return False
		i += 1
	ufhe = str.replace('/',' ').replace('*',' ').replace('-',' ').replace('+',' ').split()
	for i in ufhe:
		if i[0] in alp[2]:
			for j in i:
				if j not in alp[2]: return False
		elif i[0] in alp[1]:
			if '.' in i:
				i = i.replace('.', ' ').split()
				if len(i) > 2: return False
			for j in i:
				for k in j:
					if k not in alp[1]: return False
		else: return False
	return True
print("Алфавiт: ", ''.join(GenerateAlphabet()))
b = GenerateClassArray(GenerateAlphabet())
if CheckString(input("Введiть стрiчку: "), b):
	print("Введена стрiчка генерується даною граматикою")
else: print("Введена стрiчка не генерується даною граматикою")
system('pause')