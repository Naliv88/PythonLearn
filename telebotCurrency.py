# Технічне завдання на створення: Telegram бота для конвертації валют

# Загальна інформація
# Назва проєкту: Конвертер валют Telegram бот
# Мова програмування: Python
# Бібліотека для роботи з Telegram API: pyTelegramBotAPI
# API для отримання фінансових даних: https://api.monobank.ua/bank/currency

# Опис проєкту
# Створити Telegram бота, який надає користувачам можливість конвертувати суму з однієї валюти до іншої, 
# використовуючи фінансове API для отримання актуальних курсів валют.

# Функціонал
# Основні можливості бота:
# 1. Привітання та допомога:
# Бот вітає користувача при старті та надає інструкції щодо конвертації валют.
# 2. Конвертація валют:
# Користувач може ввести суму та обрати вихідну та цільову валюту для конвертації.
# Вихідна валюта задається за допомогою контексту (980 UAH)
# Цільова валюта здається за допомогою натискання клавіш.
# 3. Робота з файлами:
# Зберігати 10 останніх запитів на конвертацію у вигляді словника(у файлі JSON)

# Використані технології та бібліотеки
# Python 3.x
# pyTelegramBotAPI
# [Назва та версія бібліотеки для роботи з фінансовим API]

import json

# Функція для збереження запитів у файлі JSON
def save_requests(requests):
    with open('requests.json', 'w') as file:
        json.dump(requests, file)

# Функція для завантаження запитів з файлу JSON
def load_requests():
    try:
        with open('requests.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Додавання нового запиту до списку
def add_request(requests, new_request):
    requests.append(new_request)
    if len(requests) > 10:
        requests.pop(0)  # Видаляємо найстарший запит, якщо список перевищує 10 елементів
    save_requests(requests)  # Зберігаємо список у файлі JSON

# Приклад використання
requests = load_requests()
new_request = {'amount': 100, 'from_currency': 'USD', 'to_currency': 'EUR'}
add_request(requests, new_request)
