import pymongo
# from bson import Decimal128
from homework21_config import USER, PASSWORD

url = (f'mongodb+srv://{USER}:{PASSWORD}'
       '@cluster0.yuvicuz.mongodb.net/?retryWrites=true&w=majority')

client = pymongo.MongoClient(url)

db = client.DBofbooks
fantasy_literature = db.fantasy
school_literature = db.school

fantasy_literature.insert_one(
    {'name': 'Гра престолів',
     'price': 150,
     'year_of_realise': 2011,
     'number_of_pages': 500
     }
)

for_school = [
    {'_id': 1, 'name': 'Алгебра', 'class': 10, 'year_of_realise': 2017, 'number_of_pages': 200},
    {'_id': 2, 'name': 'Геометрія', 'class': 10, 'year_of_realise': 2018, 'number_of_pages': 176},
    {'_id': 3, 'name': 'Фізика', 'class': 10, 'year_of_realise': 2019, 'number_of_pages': 187},
    {'_id': 4, 'name': 'Хімія', 'class': 10, 'year_of_realise': 2021, 'number_of_pages': 223},
    {'_id': 5, 'name': 'Історія', 'class': 10, 'year_of_realise': 2021, 'number_of_pages': 150}

]
school_literature.insert_many(for_school)

result = school_literature.find_one(
    {'_id': 5}
)

# query = {}
# operation = {'$mul': {'price': Decimal128(str(1.37))}}
# data = fantasy_literature.update_many(query, operation)
# print(data.raw_result)

query = {'name': 'Гра престолів'}
operation = {'$inc': {'price': 156}}
data = school_literature.update_many(query, operation)
print(data.raw_result)

query = {'name': 'Гра престолів'}
data = fantasy_literature.delete_one(query)
print(data.raw_result)

query = {'year_of_realise': {'$lt': 2020}}
data = school_literature.delete_many(query)
print(data.deleted_count)
