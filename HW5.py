# Спочатку напишіть код для читання та аналізу даних замовлення - поділ замовлень по рядках та продуктів 
# по «@@@».
# Основний принцип конвертації даних у структурований формат буде виглядати так
# Bulgarian Yogurt@@@Organic 4% Milk Fat Whole Milk Cottage Cheese@@@Organic Celery Hearts@@@Cucumber 
# Kirby@@@Lightly Smoked Sardines in Olive Oil@@@Bag of Organic Bananas@@@Organic Hass Avocado@@@Organic Whole 
# String Cheese \n
# \n
# Grated Pecorino Romano Cheese@@@Spring Water@@@Organic Half & Half@@@Super Greens Salad@@@Cage 
# Free Extra Large Grade AA Eggs@@@Prosciutto, Americano@@@Organic Garnet Sweet Potato (Yam)@@@Asparagus

import os

script_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(script_dir, 'orders.txt')
print(file_path)

with open(file_path, 'r') as file:
    data = file.read()

lines = data.split('\n')

orders = {}

for line in lines:
    products = line.split('@@@')
    products = [product.strip() for product in products if product.strip()]
    if products:
        orders[len(orders) + 1] = products

output_file = os.path.join(script_dir, 'orders_work.txt')

with open('orders_work.txt', 'w') as file2:
    for i, (order_id, products) in enumerate(orders.items(), start=1):
        file2.write(f"\nЗамовлення {i}:\n")
        for j, product in enumerate(products, start=1):
            file2.write(f"\t{j}. {product}\n")
print("Шлях до опрацьованого файлу:", output_file)
