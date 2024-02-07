""""
У класі професора Грубла щойно був іспит. Він почав перевіряти роботи, але оцінював їх не дуже уважно.
Напишіть програму, яка приймає як вхідні дані оцінку кожного учня і те, чи здав він іспит.
Потім програмі необхідно надрукувати дві речі:
a. Чи був професор Грубл послідовним у проставленні позначки "Passed" для студентів.
b. Якщо професор Грубл був послідовним, виведіть діапазон у якому знаходиться поріг для складання іспиту.
Припустимо, ми отримуємо такі дані, як вхідні дані:
У цьому випадку професор, на жаль, непослідовний, тому що Student 6 має позначку “Passed” з оцінкою 75, а Student 1 має позначку "Failed" при вищій оцінці - 78.
Тепер припустимо, що ми отримали такі значення:
В цьому випадку професор послідовний, а поріг складання іспиту знаходиться в діапазоні 73 – 78 балів.
"""
import random
from faker import Faker

def random_student_list(stud_count):
    fake = Faker()
    students = [] 
    count = 0
    while count < stud_count:
        student = {
            "Student": fake.name() + fake.last_name(),
            "mark": random.randint(50, 100), 
            "result": random.choice(["Failed", "Passed"])
        }
        students.append(student)
        count += 1
    return students

def professor_consistent(min_passing, max_failing):
    if min_passing <= max_failing:
        print("Професор непослідовний")
    else:
        print("Професор послідовний.")
        print(f"Поріг для складання може бути в межах: {max_failing} - {min_passing}")

def min_max_marks(student_list):
    passed_list = [100]
    failed_list = [40]
    for student in student_list:
        if student['result'] == "Passed":
            passed_list.append(student["mark"])
        elif student['result'] == "Failed":
            failed_list.append(student["mark"])
    min_passing = min(passed_list)
    max_failing = max(failed_list)
    professor_consistent(min_passing, max_failing)

def valid_input(prompt):
    while True:
        try:
            value = input(prompt)
            if int(value) <= 0 or not value.isdigit():
                raise ValueError("Invalid input")
            return int(value)
        except ValueError as e:
            print(f"Error: {e}")
            continue

student_list = random_student_list(valid_input("Кількість студентів >>> "))

print(student_list)

min_max_marks(student_list)