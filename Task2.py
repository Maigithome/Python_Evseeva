# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


with open('file_encode.txt', 'w') as data:
    data.write('WWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW')

with open('file_encode.txt', 'r') as data:
    string = data.readline()

def rle_encode(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

def rle_decode(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res


with open('file_encode.txt', 'r') as file:
    txt = file.read()

with open('file_decode.txt', 'w') as file:
    encoded_string = rle_encode(txt)
    file.write(encoded_string)

print('Декодированная строка: \t' + txt)
print('Закодированная строка: \t' + rle_encode(txt))
print(f'Степень сжатия: \t{round(len(txt) / len(encoded_string), 1)}')