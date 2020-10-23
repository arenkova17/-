print('Добро пожаловать в кофейню!')
print('Выберите, пожалуйста, кофе:')
print('Кофе цена')
sort_of_coffee = [
'Черный кофе',
'Латте', 
'Капучино', 
'Эспрессо', 
'Глясе', 
'Раф' ]

price_of_coffee = [ 50, 70, 80, 60, 90, 100]


for i in range(len(sort_of_coffee)):
    print("{0:d}. {1:11} - {2:d}".format(i+1, sort_of_coffee[i], price_of_coffee[i]))

print('Выберите номер кофе')

coffee = input("Номер кофе: ")
input("Количество сахара: ")


coffee_int = int(coffee)
print("ВЫ выбрали {0:11}".format(sort_of_coffee[coffee_int-1]))

print("Введите цену кофе:")

a=int(input()) #сколько стоит руб
print("Введите купюру:")
b=int(input())  #сколько дала руб
print("Ваша сдача:")
c=b-a #сдача руб
if b>=a:
    print(c)

print("Ожидайте 5 секунд, ваш кофе готовится")

import time
time.sleep(5) 

print("Ваш кофе готово, будьте осторожны! приходите к нам снова:))")

