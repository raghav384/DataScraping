import configparser
import os

#bsolute path calculation
path_current_directory = os.path.dirname(__file__)
path_config_file = os.path.join(path_current_directory, 'ScrapingConfigurations', 'vendor_configuration.ini')

#configuration initialization
config = configparser.ConfigParser()
config.read(path_config_file)


#print(config.optiond[1])
for name, value in config.items(all_vendors):
       print(value)
``
#for section_name in config.sections():
#    print('Section:', section_name)
 #   print('Options:', config.options(section_name))
 #   for name, value in config.items(section_name):
  #      print(name,value)
   
