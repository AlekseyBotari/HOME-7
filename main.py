import random

#  Задание 1
file_1 = open('data_1.txt', 'r')
numbers = []
for i in filter(str.isdigit, file_1.read()):
    numbers.append(i)
print(numbers)
file_1.close()

# Задание 2
file_2 = open('data.txt', 'w')
file_2.write(input('Введите текст:'))
file_2.close()

# Задание 3
n_task_3 = int(input('Введите число:'))
new_list_task_3 = list(input(f'Введите {n_task_3} чисел:').split(' '))[:n_task_3]
file_3 = open('numbers.txt', 'w')
file_3.write(' '.join(map(str, new_list_task_3)))
file_3.close()

# Задание 4
file_4 = open('random_numbers.txt', 'w')
new_list_task_4 = [random.randint(1, 100) for _ in range(100)]
file_4.write('\n'.join(map(str, new_list_task_4)))
file_4.close()

# Задание 5
i = 0
file_5 = open('data_5.txt', 'r')
with file_5 as f:
    for line in f:
        for word in line.split():
            i += 1
print('Количество слов в файле:', i)
file_5.close()

# Задание 6
file_6 = open('data_6.txt', 'r')
numbers = file_6.read()
new_list_task_6 = list(map(int, numbers.split(' ')))
sum_6 = 0
for x in new_list_task_6:
    sum_6 += x
print('Сумма чисел в файле равна', sum_6)
file_6.close()

# Задание 7
file_7 = open('data_7.txt', 'r')
text = list(file_7.read())
count = {}
for x in text:
    count[x] = count.get(x, 0) + 1
doubles = {element: count for element, count in count.items() if count > 1}
file_7.close()

print(doubles)
