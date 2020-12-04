import configparser
import os
import json

#bsolute path calculation
path_current_directory = os.path.dirname(__file__)
path_config_file = os.path.join(path_current_directory, 'ScrapingConfigurations', 'vendor_configuration.ini')

#configuration initialization
config = configparser.ConfigParser()
config.read(path_config_file)


#print(config.optiond[1])
#for section_name in config.sections():
 ##   for name, value in config.items("all_vendors"):
   #    print(value)

print(json.loads(config.get("pharmeasy","key_dictionary")))
vendor_list = json.loads(config.get("all_vendors","vendors_list"))
print(vendor_list)

vendor ="pharmeasy"
print(int(config[vendor]["start_product_id"]))
#for section_name in config.sections():
#    print('Section:', section_name)
 #   print('Options:', config.options(section_name))
 #   for name, value in config.items(section_name):
  #      print(name,value)
   
