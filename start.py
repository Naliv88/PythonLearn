import datetime
print("hello")

# # введіть числа
# a = input("a=") # приймає тільки рядок (символи)
# b = input("b=")
# print("2. ", a + b) # !!!
# # введіть числа
# a = int(input("a=")) # приймає числа
# b = int(input("b="))
# print("3. ", a + b)

# а[start:stop:step]

mylist = ["apple", "banana", "cherry"]
print(mylist[0])

# S.isdigit() Чи складається рядок із цифр
# S.isalpha() Чи складається рядок з літер

print(id(mylist))

# # Умовна конструкція
# x = 10
# if x > 0:
# print("x є додатним числом")
# elif x < 0:
# print("x є від'ємним числом")
# else:
# print("x дорівнює нулю")
# # Цикл for
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
# print(fruit)
# # Цикл while
# count = 0
# while count < 5:
# print(count)
# count += 1
# # Виключення
# try:
# result = 10 / 0
# except ZeroDivisionError:
# print("Ділення на нуль не допустиме")
# finally:
# print("Завершення програми")

# # Додавання елемента до списку
# fruits.append('mango')
# print(fruits) # Виведе: ['apple', 'pear', 'orange', 'grape', 'mango']
# [1,2,3].append([4,5]) == [1,2,3,[4,5]]
# [1,2,3].extend([4,5]) == [1,2,3,4,5]


# # Видалення елемента зі списку
# del fruits[2]
# print(fruits) # Виведе: ['apple', 'pear', 'grape', 'mango']

# help(list)
# print(dir(mylist))
# print(type(mylist), type("ssdf"), type(234))

# result = eval("2 + 3 * 4")
# result = 2 + 3 * 4
# print(result)

# data = "{1:'one'}"
# print(data[1]) # 1, бо у рядку за цим індексом символ "1"
# data = eval(data)
# print(data[1]) # "one", бо у словнику за ключем таке значення

# def process_data(data):
#     match data:
#         case 0:
#             print("Нуль")
#         case 1:
#             print("Один")
#         case _:
#             print("Інше число")

# # Вивести числа від 0 до 4
# for i in range(5):
# print(i)
# # Вивести парні числа від 0 до 10
# for i in range(0, 11, 2):
# print(i)
# # Створити список чисел від 1 до 5
# numbers = list(range(1, 6))
# print(numbers)

print(datetime.datetime.now())
# Перетворення рядка на об'єкт datetime
date_string = "2022-01-01"
converted_datetime = datetime.datetime.strptime(date_string, "%Y-%m-%d")
print("Перетворений об'єкт datetime:", converted_datetime)