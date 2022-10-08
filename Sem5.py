# def fib(n):
#     if n in [1, 2]:
#         return 1
#     if n < 0:
#         return fib(-n) * (-1) ** (-n+1)
#     else:
#         return fib(n-1) + fib(n-2)

# 32.	Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности

converted_list = list(map(int, input().split()))
filtered_list = list(filter(lambda x: converted_list.count(x) == 1, converted_list)) # фильтр оставил те элементы, которые встречаются один раз и не повторяются True
print(filtered_list)

# или

converted_list = list(map(int, input().split()))
filtered_list = [x for x in converted_list if converted_list.count(x) == 1]
print(filtered_list)



# 22.	Найти сумму чисел списка стоящих на нечетной позиции

filtered_list = [x for x in converted_list if x % 2 == 0] # находит элементы на нечетных позициях

# 12.	Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.

a = [3*n + 1 for n in range(10)]
d = {}
for idx, el in enumerate(a):
    d.update({idx: el})
print(d)

# или

d = {n: 3*n+1 for n in range(1, 10)}
print(d)


# 35. В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного,
# чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.


# path = 'list.txt'  # путь к папке
# data = open(path, 'r')  # откроем в режиме чтения
# list_number = data.readline()
# data.close()
# list_number = list(map(int, list_number.split()))
# print(list_number)
#
# for i in range(1, len(list_number)):
#     if not list_number[i] -1 == list_number[i-1]:
#         print(f" {list_number[i] -1}")


with open('list.txt', 'r', encoding='utf-8') as data:
    a = data.read().split()
    a = list(map(int, a))
print(a)

for i in range(1, len(a)):
    if a[i] - 1 != a[i-1]:
        print(int(a[i-1]) + 1)


# 38. Напишите программу, удаляющую из текста все слова содержащие "абв".

text = str('абвольт (абв) — единица измерения электрического потенциала (напряжения),\
разности электрических потенциалов и электродвижущей силы (ЭДС) в СГСМ\
(абсолютной электромагнитной системе сантиметр-грамм-секунда). 1 абвольт\
равен 10–8 В. При разности потенциалов в 1 абвольт через сопротивление\
1 абом будет протекать ток силой 1 ампер. Для перемещения заряда величиной\
в 1 абкулон между двумя точками с разностью потенциалов 1 вольт требуется\
энергия в 1 эрг.')

search_text = 'абв'
print(f'Текст до обработки:\n{text}')
print(f'\nУдалаяем из текста слова содержащие: \'{search_text}\'\n')
lst = (" ".join([el for el in text.split() if search_text not in el]))
print(f'Текст после обработки:\n{lst}\n\n')


my_text = 'Напишите абв напиабв програбвмму программу, удаляющую из этого абв текста все вабвс слова, содерабващие содержащие "абв"'

def del_some_words(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    print(my_text)
    return " ".join(my_text)

my_text = del_some_words(my_text)
print(my_text)
