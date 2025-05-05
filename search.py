# Программа для чтения всех строк в файле с помощью функции readline()
# file = open("ПрисоединенныйФайлАнтей.txt", "r")
# while True:
	# content=file.readline()
	# if not content:
		# break
	# print(content)
# file.close()


import io
import os
import sys

if len(sys.argv) > 1:
	f_antey = sys.argv[1]
	f_stock = sys.argv[2]
else:
	cwd = os.getcwd()
	print('Программа поика строковых значений в файле строк поиска')
	print('EXAMPLE:\n', cwd + ">py search.py ФайлССтрокамиПоиска.txt ФайлСтрокПоиска.txt")
	quit()

spisok = []

with io.open(f_antey, encoding='utf-8') as file:
	for line in file:
		index = 0
		with io.open(f_stock, encoding='utf-8') as file_s:
			for line_s in file_s:
				if line == line_s:
					index = 1
		if index == 0:
			spisok.append(line.strip())
			# print(line)

if len(spisok) > 0:
	distance = 35 + len(f_stock)
	str_simbol = ''
	for i in range(distance):
		str_simbol += '='
	print(str_simbol)
	print('Список отсутвующих строк в файле: ', f_stock)
	print(str_simbol)
	for i in range(len(spisok)):
		print(spisok[i])




# spisok = ["один", "два", "три", "четыре", "пять"];
# n_spisok = []
# import os
# import subprocess
# import sys
	

# cwd = os.getcwd()
# f1 = open(cwd + '\ПрисоединенныйФайлАнтей.txt', 'r', encoding='utf8')

# f1 = open('ПрисоединенныйФайлАнтей.txt')
# s_out = f1.read()
# print(s_out)
# f1.close()
# print(f1.closed)

# for i in range(len(s_out)):
    # s_tmp = s_out[i].split()
    # s_tmp[0] = spisok[i]
    # n_spisok.append(' '.join(s_tmp))
	# print(s_out[i])

# for i in range(len(n_spisok)):
    # n_spisok[i] = n_spisok[i] + '\n'
    # print(n_spisok[i])
# print(n_spisok)

# f2 = open('./dataRu.txt', 'w')
# f2.writelines(n_spisok)
# f2.close()
# print(f2.closed)