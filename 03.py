#Задайте последовательность чисел. 
#Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

a = [1, 33, 5, 1, 55, 2]# задали список сами
print(a)# вывели этот список
new_a = []# оброзначили новый список
for i in a:# проходим по заданному списку
    if i not in new_a:# если элемента из заданного списка нет в новом, 
        new_a.append(i)# то мы его записываем в новый список
print(new_a)#