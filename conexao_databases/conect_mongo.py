from pymongo import MongoClient
from pprint import pprint
from bson import ObjectId
from faker import Faker
from datetime import datetime
from time import sleep
try:
    client = MongoClient()
    db = client['projeto']

except Exception as e:
    print('Erro:{}'.format(e))
    exit()
print(datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
fake = Faker('pt-BR')


# for x in  range(5000):
#     registro = {'nome': fake.name(), 'cpf': fake.cpf(), 'endereço': fake.address()}
#     db.pessoas.insert(registro)

print(datetime.now().strftime('%d-%m-%Y %H:%M:%S'))

# ling = {'daniel': 'python', 'hector': 'php', 'joao': 'javascript'}

# db.teste.insert(ling)

for x in db.pessoas.find():
    pprint(x)
    sleep(1)
# db.usuarios.insert({"nome":"josé"})
# db.usuarios.remove({'_id': ObjectId('5ba64fc994252b4d4afb15e7')})
# pprint()
