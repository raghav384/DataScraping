from pymongo import MongoClient
import pickle
from datetime import datetime

def mongo_insert(input_data):
    try:
        client = MongoClient("mongodb://localhost:27017/")
        database = client.medicine_data
        collection = database.medicine_record_data
        data_list = []
        for i in input_data.keys():
            data_list += input_data[i]
           
        for i in range(len(data_list)):
            #print(type(data_list[i]))
            try:
                now = datetime.now()
                data_list[i]['time_of_insertion'] = now 
                collection.insert_one(data_list[i])
            except:
                print("ERROR:",data_list[i])
    except:
        print("Data not inserted , temportary bin file created with list_data")
        filename = 'list_data'
        outfile = open(filename,'wb')
        pickle.dump(input_data,outfile)
        outfile.close()    


def mongo_insert_multi_thread(input_data):
    try:
        client = MongoClient("mongodb://localhost:27017/")
        database = client.medicine_data
        collection = database.medicine_record_data
                 
        for i in range(len(input_data)):
            #print(type(data_list[i]))
            try:
                now = datetime.now()
                input_data[i]['time_of_insertion'] = now 
                collection.insert_one(input_data[i])
            except:
                print("ERROR:",input_data[i])
    except:
        print("Data not inserted , temportary bin file created with list_data")
        filename = 'list_data'
        outfile = open(filename,'wb')
        pickle.dump(input_data,outfile)
        outfile.close()    
