# Задача 29:
# Ваня и Петя поспорили, кто быстрее решит следующую задачу:
# “Задана последовательность неотрицательных целых чисел.
# Требуется определить значение наибольшего элемента последовательности, которая завершается первым встретившимся нулем
# (число 0 не входит в последовательность)”.
# Однако 2 друга оказались не такими смышлеными. Никто из ребят не смог до конца сделать это задание.
# Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор. За помощью товарищи обратились к Вам, студентам.

from random import randint
n = 20
sequence = [randint(0,15) for i in range(n)]
print(sequence)
max = sequence[0]

for i in range(n):
    if sequence[i] > max and sequence[i] > 0:
        max = sequence [i]
    elif sequence [i] == 0:
        if max > 0:
            print(max)
        max = 0
if max > 0:
    print(max)