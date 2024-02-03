point_hw = input("Введіть пункт домашнього завдання 1-5 >>> ")

def process_data(data: int):
    glossary=[["foo", "bar", "ham"],["Перше число більше за друге", "Друге число більше за перше"], ["fizz", "buzz", "fizz buzz"], "BOOM"]
    match data:
        case 1:
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
            num_1, num_2=[int(input("Введіть перше ціле число >>> ")), int(input("Введіть друге ціле число >>> "))]
            print(glossary[1][0]) if num_1>num_2 else print(glossary[1][1]) 
        case 3:
            num_3 = [int(input("Введіть перше ціле число >>> ")), int(input("Введіть друге ціле число >>> ")), int(input("Введіть трете ціле число >>> "))]
            sorted_num_3 =sorted(num_3)
            print(f"Найменьше число {sorted_num_3[0]}\n", f"Середне число {sorted_num_3[1]}\n", f"Найбільше число {sorted_num_3[2]}")
        case 4:
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
