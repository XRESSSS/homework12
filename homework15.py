import requests

url = ''

data = requests.get(url)

data_dict = data.json()

total_cost = sum([product['price'] * product['remainder'] for product in data_dict['shop']])
total_cost_without_gluten = sum(
    [product['price'] * product['remainder'] for product in data_dict['shop'] if not product['contains_gluten']])

print(f'Сумма всех товаров {total_cost} гривен')
print(f'Сумма всех товаров без глютена {total_cost_without_gluten} гривен')
