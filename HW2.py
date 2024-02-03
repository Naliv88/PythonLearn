point_hw = input("Введіть пункт домашнього завдання 1-6 >>> ")

def process_data(data: int):
    glossary=[["foo", "bar", "ham"],["Перше число більше за друге", "Друге число більше за перше"], ["fizz", "buzz"], "BOOM"]
    match data:
        case 1:
            number=int(input("Введіть ціле число >>> "))
            if number%3==0 and number%5==0: print(glossary[0][0])
            if number%3==0: print(glossary[0][0])
            if number%5==0: print(glossary[0][1])
        case 2:
            num_1, num_2=[int(input("Введіть ціле first число >>> ")), int(input("Введіть ціле second число >>> "))]
            print(glossary[1][0]) if num_1>num_2 else print(glossary[1][1]) 
        case _:
            print("Інше число")

if point_hw.isnumeric():
    point_hw = int(point_hw)
    process_data(point_hw)
else:
    print("Введено не число")
