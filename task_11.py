# Задача №11:
# Дано натуральное число A > 1.
# Определите, каким по счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.

#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
#0__1__2__3__4__5__6__7___8___9___10__11
# Input: 5
# Output: 6

number = int(input("Enter number: "))
s1 = 0
s2 = 1
s3 = 1
n = 2
while s3 < number:
    s1 = s2
    s2 = s3
    s3 = s1 + s2
    n += 1

if s3 == number:
    print(n)
else:
    print(-1)
