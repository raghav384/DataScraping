import requests
import io
import json
from pymongo import MongoClient
import pickle
from datetime import datetime
import concurrent.futures

def mongo_insert_dict(input_data):
    try:
        client = MongoClient("mongodb://localhost:27017/")
        database = client.pharmeasy_medicine_data
        collection = database.medicine_records
                 
        for i in range(len(input_data)):
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

medicine_records = []
def get_medicine_record(product_id):
    try:
        print("Medicine no",product_id)
        product_desc_url = "https://pharmeasy.in/api/productDescription/fetchProductDescription/"+ str(product_id)
        response = requests.get(product_desc_url)
        response_json_content =json.loads(response.content)
        response_data_dict = response_json_content["data"]
        key_values_dict = [ "productId","name","fullManufacturerName","measurementUnit",
                            "packform","isRxRequired","isRefrigerated","isChronic","mrpDecimal",
                            "salePriceDecimal","discountDecimal","discountPercent","medicineStatusFlags",
                            "availableQuantity","isAvailable","composition","therapy","pricePerUnit","returnText"
                        ]
        medicine_data_record = {key:response_data_dict[key] for key in  response_data_dict.keys() & key_values_dict }
        medicine_records.append(medicine_data_record)
    except:
        print("Exception occured !!!")

with concurrent.futures.ThreadPoolExecutor(max_workers=12) as executor:
    futures= []
    for i in range(1,40001):
        futures.append(executor.submit(get_medicine_record, i))

print("Database insertion starts")
print(len(medicine_records))
mongo_insert_dict(medicine_records)
print("Database insertion ends")

