import pymongo
import json
import configparser

client = pymongo.MongoClient("mongodb://localhost:27017/")
config = configparser.ConfigParser()
config.read('./vendor_configuration.ini')

db = client["HealthScrollDB"]
col = db["vendor_api_details"]
x = col.find({"status":"pending_for_insertion"})
for data in x:
    vendor_name = data["vendor_api_data"]["vendor_name"]
    api_base_url = data["vendor_api_data"]["api_base_url"]
    start_product_id = data["vendor_api_data"]["product_id_start"]
    end_product_id = data["vendor_api_data"]["product_id_end"]
    
    key_values_dict = json.loads(config.get("pharmeasy","key_dictionary"))
    keywords = "["
    for i in key_values_dict:
        keywords = keywords + '"' + i + '"' + ","
    keywords =keywords[:-1]
    keywords  = keywords + "]"

    config.add_section(vendor_name)
    config.set(vendor_name, 'api_base_url', api_base_url)
    config.set(vendor_name, 'start_product_id', start_product_id)
    config.set(vendor_name, 'end_product_id', end_product_id)
    config.set(vendor_name, 'key_dictionary', keywords)

    no_of_vendors = config.getint("all_vendors","no_of_vendors")
    vendors_list = config.get("all_vendors","vendors_list")
    vendors_list =vendors_list[:-1]
    vendors_list = vendors_list + "," + '"' +vendor_name +'"' + "]";

    config.set("all_vendors", 'no_of_vendors', str(no_of_vendors+1))
    config.set("all_vendors", 'vendors_list', vendors_list)
    
with open('vendor_configuration.ini', 'w') as configfile:    # save
    config.write(configfile)

update_search_find= { "status": "pending_for_insertion" }
status_update = { "$set": { "status": "api_details_inserted" } }

y = col.update_many(update_search_find, status_update)
print(y.modified_count, "documents updated.")