# Спочатку напишіть код для читання та аналізу даних замовлення - поділ замовлень по рядках та продуктів 
# по «@@@».
# Основний принцип конвертації даних у структурований формат буде виглядати так
# Bulgarian Yogurt@@@Organic 4% Milk Fat Whole Milk Cottage Cheese@@@Organic Celery Hearts@@@Cucumber 
# Kirby@@@Lightly Smoked Sardines in Olive Oil@@@Bag of Organic Bananas@@@Organic Hass Avocado@@@Organic Whole 
# String Cheese \n
# \n
# Grated Pecorino Romano Cheese@@@Spring Water@@@Organic Half & Half@@@Super Greens Salad@@@Cage 
# Free Extra Large Grade AA Eggs@@@Prosciutto, Americano@@@Organic Garnet Sweet Potato (Yam)@@@Asparagus

import requests
import os
from tqdm import tqdm
from itertools import combinations
from collections import Counter
import logging

logging.basicConfig(level=logging.INFO)

MIN_SUPPORT = 15
MIN_CONFIDENCE = 45
FILE_NAME = "orders.txt"
DOCUMENT_URL = "https://drive.google.com/uc?export=download&id=1IOPTVq2ooQfZRkF3rAjGkTjRtbotG7FF"

from tqdm import tqdm

def download_document(file_name, document_url):
    if os.path.exists(file_name):
        return read_orders(file_name)
    else:
        download = input("Файл ордер не знайдено. Чи бажаєте ви завантажити його? (так/ні): ")
        if download.lower() == 'так':
            response = requests.get(document_url, stream=True)
            if response.status_code == requests.codes.ok:
                total_size_in_bytes= int(response.headers.get('content-length', 0))
                block_size = 1024 #1 Kibibyte
                progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
                with open(file_name, 'wb') as f:
                    for data in response.iter_content(block_size):
                        progress_bar.update(len(data))
                        f.write(data)
                progress_bar.close()
                if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
                    logging.error("ERROR, something went wrong")
                return read_orders(file_name)
            else:
                logging.error(f'Failed to download the document. Status code: {response.status_code}')
                return None
        else:
            return None

def read_orders(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    orders = [line.strip().split('@@@') for line in content.split('\n\n') if line.strip()]
    
    return orders

product_count = Counter()
pair_count = Counter()

def count_products(orders):
   
    for order in tqdm(orders, desc="Підрахунок продуктів"):
        for product in order:
            product_count[product] += 1

def count_pairs(orders):
   
    for order in tqdm(orders, desc="Підрахунок пар"):
        for pair in combinations(sorted(set(order)), 2):
            pair_count[pair] += 1

def find_association_rules(orders):
    
    rules = []
    for (product1, product2), pair_freq in tqdm(pair_count.items(), desc="Пошук асоціативних правил"):
        product1_freq = product_count[product1]
        product2_freq = product_count[product2]
        confidence_product1_to_product2 = (pair_freq / product1_freq) * 100
        confidence_product2_to_product1 = (pair_freq / product2_freq) * 100
        support = pair_freq

        if support >= MIN_SUPPORT:
            if confidence_product1_to_product2 >= MIN_CONFIDENCE:
                rules.append(f"{product1} => {product2}: Support = {support}, Confidence = {confidence_product1_to_product2:.2f}%")
            if confidence_product2_to_product1 >= MIN_CONFIDENCE:
                rules.append(f"{product2} => {product1}: Support = {support}, Confidence = {confidence_product2_to_product1:.2f}%")
    
    return rules

if __name__ == "__main__":
    orders = download_document(FILE_NAME, DOCUMENT_URL)
    count_products(orders)
    count_pairs(orders)
    association_rules = find_association_rules(orders)
    print(f"Всього правил: {len(association_rules)}")
    result = input("Вивести всі асоціації? (так/ні): ")
    if result.lower() == 'так':
        for rule in association_rules:
            print(rule)

