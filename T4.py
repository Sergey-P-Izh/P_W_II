#Задача 4: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

print ('n, введите число, которое требуется возвести в степень')
n = int(input())
i = 0
while i < n:
    print(n**i)
    i = i+1 