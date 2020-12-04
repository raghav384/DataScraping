import requests
import io
import json
from pymongo import MongoClient
import pickle
from datetime import datetime
import concurrent.futures
import configparser
import os

#absolute path calculation
path_current_directory = os.path.dirname(__file__)
path_config_file = os.path.join(path_current_directory, 'ScrapingConfigurations', 'vendor_configuration.ini')

#configuration initialization
config = configparser.ConfigParser()
config.read(path_config_file)

def mongo_insert_dict(input_data):
    try:
        client = MongoClient(config["mongodb"]["host_url"])
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
def get_medicine_record(vendor, product_id):
    try:
        print("Medicine no",product_id)
        product_desc_url = config[vendor]["api_base_url"] + str(product_id)
        response = requests.get(product_desc_url)
        response_json_content =json.loads(response.content)
        response_data_dict = response_json_content["data"]
        key_values_dict = json.loads(config.get(vendor,"key_dictionary"))
        medicine_data_record = {key:response_data_dict[key] for key in  response_data_dict.keys() & key_values_dict }
        medicine_records.append(medicine_data_record)
        print(medicine_data_record)
    except:
        print("Exception occured !!!")


#vendor_list = json.loads(config.get("all_vendors","vendors_list"))
vendor_list = ["pharmeasy"]
for vendor in vendor_list:
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        futures= []
        start = config[vendor]["start_product_id"]
        end = config[vendor]["end_product_id"]
        for i in range(int(start),int(end)):
            futures.append(executor.submit(get_medicine_record, vendor,i))

#print(len(medicine_records))

print("Database insertion starts")
#mongo_insert_dict(medicine_records)
print("Database insertion ends")

