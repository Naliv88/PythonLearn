point_hw = input("Введіть пункт домашнього завдання 1-4 >>> ")

if point_hw.isdigit():
    point_hw_int=int(point_hw)
    # Home work 1.1
    if point_hw_int == 1:
        hw_list1=[input("Введіть ім'я >>> "), int(input("Введіть зарплату >>> "))]
        salary_year = int(hw_list1[1] * 12 / 1000)
        print(f"Річна зарплата {hw_list1[0]} складає {salary_year} тис. доларів")
    # Home work 1.2
    elif point_hw_int == 2:
        int_number = int(input("Введіть ціле число >>> "))
        if 100 < int_number < 999 and int_number % 2 == 0:  
            print("True\n", "Це парне число в діапазоні від 100 до 999") 
        else:
            print("False\n", "Це НЕ парне число в діапазоні від 100 до 999")
    # Home work 1.3  
    elif point_hw_int == 3:
        number_3= input("Введіть ціле число від 101 до 999 (його остання цифра не може бути 0) >>> ")
        if int(number_3[-1]) != 0 and 101 <= int(number_3) <= 999:
            print(f"Реверс: {number_3[::-1]}")
        else :
            print("Невірно введене число")
    # Home work 1.4
    elif point_hw_int == 4:
        hw_list2=[int(input("Введіть перше число >>> ")), int(input("Введіть друге число >>> "))]
        print(f"\n Cумма {hw_list2[0]+hw_list2[1]} \n Різниця {hw_list2[0]-hw_list2[1]}\n Результат множення {hw_list2[0]*hw_list2[1]}\n Результат поділу першого на друге {hw_list2[0]/hw_list2[1]}\n Залишок від поділу першого на друге {hw_list2[0]%hw_list2[1]}\n {hw_list2[0]>hw_list2[1]}")
    else:
        print("Номер такого завдання відсутній або це не число від 1 до 4")
else:
    print("Введено не число")

