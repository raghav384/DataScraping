from pymongo import MongoClient

def mongo_insert(input_data):
    client = MongoClient("mongodb://localhost:27017/")
    database = client.PharmEasyDB
    collection = database.MedicinesData
    data_list = []
    for i in input_data.keys():
        data_list.append(input_data[i])
    collection.insert(data_list)
