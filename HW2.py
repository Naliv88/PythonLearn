point_hw = input("Введіть пункт домашнього завдання 1-5 >>> ")

def process_data(data: int):
    glossary=[["foo", "bar", "ham"],["Перше число більше за друге", "Друге число більше за перше"], ["fizz", "buzz", "fizz buzz"], "BOOM"]
    match data:
        case 1:
            print('Завдання 1: Як вхідні дані запитайте ціле число. Якщо воно ділиться на 3, виведіть "foo"; якщо воно ділиться на 5, виведіть "bar"; якщо воно ділиться на обидва, виведіть "ham" (а не "foo" або "bar").')
            number=int(input("Введіть ціле число >>> "))
            if number % 3 == 0 and number % 5 == 0:
                print(glossary[0][2])
            elif number % 3 == 0:
                print(glossary[0][0])
            elif number % 5 == 0:
                print(glossary[0][1])
            else:
                print("Число не ділеться на 3 або 5")
        case 2:
            print('Завдання 2: Як вхідні дані запитайте два числа та виведіть яке з них менше і яке більше')
            num_1, num_2=[int(input("Введіть перше ціле число >>> ")), int(input("Введіть друге ціле число >>> "))]
            print(glossary[1][0]) if num_1>num_2 else print(glossary[1][1]) 
        case 3:
            print('Завдання 3: Як вхідні дані запитайте три числа і виведіть найменше, середнє та найбільше. Припустимо, всі вони різні')
            num_3 = [int(input("Введіть перше ціле число >>> ")), int(input("Введіть друге ціле число >>> ")), int(input("Введіть трете ціле число >>> "))]
            sorted_num_3 =sorted(num_3)
            print(f"Найменьше число {sorted_num_3[0]}\n", f"Середне число {sorted_num_3[1]}\n", f"Найбільше число {sorted_num_3[2]}")
        case 4:
            print('Завдання 4: Зіграйте у гру Fizz-Buzz: виведіть усі числа від 1 до 100; якщо число ділиться на 3, замість числа виведіть "fizz". Якщо воно ділиться на 5, замість числа виведіть "Buzz". Якщо воно ділиться на обидва, виведіть "fizz buzz" замість числа.')
            list=[]
            for x in range(1, 101):
                if x % 3 ==0 and x%5==0:
                     list.append(glossary[2][2])
                     continue
                if x%5==0:
                    list.append(glossary[2][1])
                    continue
                if x % 3 ==0:
                    list.append(glossary[2][0])
                    continue
                list.append(x)
            print(list)
        case 5:
            print('Завдання 5: Зіграйте у гру 7-boom: виведіть усі числа від 1 до 100; якщо число ділиться на 7 або містить цифру 7, виведіть "BOOM" замість числа.')
            list=[]
            for x in range(1, 101):
                if x % 7 ==0 or "7" in str(x):
                     list.append(glossary[3])
                     continue
                list.append(x)
            print(list)
        case _:
            print("Інше число")


if point_hw.isnumeric():
    point_hw = int(point_hw)
    process_data(point_hw)
else:
    print("Введено не число")
