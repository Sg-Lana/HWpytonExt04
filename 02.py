#Задайте натуральное число N. 
#Напишите программу, которая составит список простых множителей числа N.

num = int(input("Введите число: "))
i = 2  # первое простое число
lst = []
while i <= num: #пока простой множитель меньше или равен заданному числу
    if num % i == 0: # если число делиться на первый простой множитель i без остатка
        lst.append(i) # то i записываем в список
        num //= i #число делим опять на i, получаем следующее с которым будем работать
        i = 2 # простой множитель оставляем 2
    else:
        i += 1
print(f"Простые множители числа это: {lst}")
