import requests
from bs4 import BeautifulSoup
from database_functions import mongo_insert_multi_thread
import concurrent.futures
import string

medicine_records_list = []
def find_all_medicine_urls(website_url):
    global medicine_records_list
    output_response = requests.get(current_url)
    soup = BeautifulSoup(output_response.content,'html.parser')
    print(soup)
    output = soup.find_all("div",{"class":"Card_container2Kvce CardproductCard2MScM Carddirection_1UZ-g container-fluid-padded-xl"})
    print(len(output))
    #for i in range(len(output)):
        #medicine_url = "https://www.1mg.com" +  str(output[i].a['href'])
        #medicine_records_list.append(get_medicine_record(output[i],medicine_url))



def get_medicine_record(content,link):
    
    medicine_data_record ={}
    medicine_data_record['vendor_name'] = '1mg'
    medicine_data_record['medicine_url'] = link
    try:
        medicine_data_record['medicine_name'] =  content.span.contents[0].text
        
    except:
        medicine_data_record['medicine_name'] = str(content)
        medicine_data_record['error_found'] = []
        medicine_data_record['error_found'].append('medcine_name not in order')
    try:
        medicine_data_record['medicine_manufacturer'] = content.span.contents[3].text
    except:
        medicine_data_record['medicine_manufacturer'] = str(content)
        if 'error_found' in medicine_data_record.keys():
            medicine_data_record['error_found'].append('medcine_manufacturer not in order')
        else:
            medicine_data_record['error_found'] = []
            medicine_data_record['error_found'].append('medcine_manufacturer not in order')

    try:
        medicine_data_record['medicine_number_of_strips'] = content.span.contents[2].text
    except:
        medicine_data_record['medicine_number_of_strips'] = str(content)
        if 'error_found' in medicine_data_record.keys():
            medicine_data_record['error_found'].append('medcine_strip not in order')
        else:
            medicine_data_record['error_found'] = []
            medicine_data_record['error_found'].append('medcine_strip not in order')
    try:
        medicine_data_record['medicine_price'] = float(content.span.contents[5].text.split("₹")[1])
    except:
        medicine_data_record['medicine_price'] = str(content)
        if 'error_found' in medicine_data_record.keys():
            medicine_data_record['error_found'].append('medcine_price not in order')
        else:
            medicine_data_record['error_found'] = []
            medicine_data_record['error_found'].append('medcine_price not in order')

    
    try:
        medicine_data_record['medicine_composition'] = content.span.contents[4].text
    except:
        medicine_data_record['medicine_composition'] = str(content)
        if 'error_found' in medicine_data_record.keys():
            medicine_data_record['error_found'].append('medcine_composition not in order')
        else:
            medicine_data_record['error_found'] = []
            medicine_data_record['error_found'].append('medcine_composition not in order')
    return medicine_data_record        




website_url= "https://www.1mg.com/drugs-all-medicines"


for i in list(string.ascii_lowercase):
    for j in range(1,50):
        current_url = website_url + "?page="+ str(j) +"&label=" + i
        print(current_url)
        find_all_medicine_urls(current_url)

#input_data = medicine_records_list.copy()
#mongo_insert_multi_thread(medicine_records_list)
