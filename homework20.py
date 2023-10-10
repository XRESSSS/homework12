# 1
import requests
import json

url = 'https://script.google.com/macros/s/AKfycbwQtueB9osOYpDA6XpR_hNTxiTH5TaakVRj6smrDaQEltP4r7TLmaxT4Ai1hmwp14U5/exec'

data = requests.get(url)

data_dict = data.json()

with open('jsdata.json', mode='w', encoding='utf-8') as file:
    json.dump(data_dict, file)

# 2

sort = [1, 3, 2, 5, 4, 1.7, 2.7]
result = map(lambda data1: str(data1), sort)
print(list(result))

# 3

sort2 = [1, 2, 3, 4, 5, 2.7, 1.7, 1.77]

def sort_int_numbers(value):
    return type(value) == int

result2 = filter(sort_int_numbers, sort2)
print(list(result2))
