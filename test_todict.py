#!/usr/bin/python3

from models.base_model import BaseModel
from models import storage

diccionario= BaseModel()

all_objects = storage.all()

lista_objetos =[]

#for value in all_objects:
#    lista_objetos += [value.__str__()]

if str("BaseModel.6034fbde-1c97-4754-88e0-d4107df0587e") not in all_objects:
    print("aqui no toy")
else:
    print("aqui toy")

# print("_____lidta de objetos:")
# print(lista_objetos)