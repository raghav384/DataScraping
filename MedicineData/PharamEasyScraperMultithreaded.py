import requests
from bs4 import BeautifulSoup
from database_functions import  mongo_insert_multi_thread
import concurrent.futures
import string

medicine_records = []
def find_all_medicine_urls(webiste_url):
    url = current_url + '0'
    output_response = requests.get(url)
    soup = BeautifulSoup(output_response.content,'html.parser')
    output = soup.findAll("div",{"class":"U9o7k"})
    name_list = []
    for i in range(len(output)):
        medicine_url = "https://pharmeasy.in" +  str(output[i].a['href'])
        name_list.append(medicine_url)
    return name_list

def get_medicine_record(medicine_url):
    global medicine_records
    medicine_response = requests.get(medicine_url)
    medicine_data_soup = BeautifulSoup(medicine_response.content,'html.parser')
    medicine_data_record ={}
    medicine_data_record['Vendor_Name'] = 'pharmaEasy'
    try:
        medicine_data_record['medicine_name'] = medicine_data_soup.find("h1",{"class":"ooufh"}).text
    except:
        medicine_data_record['medicine_name'] = str(medicine_data_soup.find("h1",{"class":"ooufh"}))
        medicine_data_record['error_found'] = []
        medicine_data_record['error_found'].append('medcine_name not in order')
    try:
        medicine_data_record['medicine_producer'] = medicine_data_soup.find("div",{"class":"_3JVGI"}).text
    except:
        medicine_data_record['medicine_producer'] = str(medicine_data_soup.find("div",{"class":"_3JVGI"}))
        if 'error_found' in medicine_data_record.keys():
            medicine_data_record['error_found'].append('medcine_producer not in order')
        else:
            medicine_data_record['error_found'] = []
            medicine_data_record['error_found'].append('medcine_producer not in order')

    try:
        medicine_data_record['medicine_number_of_strips'] = int(medicine_data_soup.find("div",{"class":"_36aef"}).text.split(" ")[0])
    except:
        medicine_data_record['medicine_number_of_strips'] = str(medicine_data_soup.find("div",{"class":"_36aef"}))
        if 'error_found' in medicine_data_record.keys():
            medicine_data_record['error_found'].append('medcine_strip not in order')
        else:
            medicine_data_record['error_found'] = []
            medicine_data_record['error_found'].append('medcine_strip not in order')
    try:
        medicine_data_record['medicine_price'] = medicine_data_soup.find("div",{"class":"_1_yM9"}).text
    except:
        medicine_data_record['medicine_price'] = str(medicine_data_soup.find("div",{"class":"_1_yM9"}))
        if 'error_found' in medicine_data_record.keys():
            medicine_data_record['error_found'].append('medcine_price not in order')
        else:
            medicine_data_record['error_found'] = []
            medicine_data_record['error_found'].append('medcine_price not in order')

    try:
        medicine_data_record['medicine_vendor_price'] =  float(medicine_data_soup.find("div",{"class":"_3FUtb"}).text.split("₹")[1])
    except:
        medicine_data_record['medicine_vendor_price'] =  str(medicine_data_soup.find("div",{"class":"_3FUtb"}))
        if 'error_found' in medicine_data_record.keys():
            medicine_data_record['error_found'].append('medcine_vendor_price not in order')
        else:
            medicine_data_record['error_found'] = []
            medicine_data_record['error_found'].append('medcine_vendor_price not in order')

    try:
        medicine_data_record['medicine_dicount'] = float(medicine_data_soup.find("div",{"class":"_306Fp"}).text.split("%")[0])
    except:
        medicine_data_record['medicine_dicount'] = str(medicine_data_soup.find("div",{"class":"_306Fp"}))
        if 'error_found' in medicine_data_record.keys():
            medicine_data_record['error_found'].append('medcine_discount not in order')
        else:
            medicine_data_record['error_found'] = []
            medicine_data_record['error_found'].append('medcine_discount not in order')
    try:
        medicine_data_record['medicine_composition'] = medicine_data_soup.find("div",{"class":"_3Phld"}).text
    except:
        medicine_data_record['medicine_composition'] = str(medicine_data_soup.find("div",{"class":"_3Phld"}))
        if 'error_found' in medicine_data_record.keys():
            medicine_data_record['error_found'].append('medcine_composition not in order')
        else:
            medicine_data_record['error_found'] = []
            medicine_data_record['error_found'].append('medcine_composition not in order')

    try:
        medicine_data_record['medicine_theuraptic_Classification'] = medicine_data_soup.find("td",{"class":"_3C_XR"}).text
    except:
        medicine_data_record['medicine_theuraptic_Classification'] = str(medicine_data_soup.find("td",{"class":"_3C_XR"}))
        if 'error_found' in medicine_data_record.keys():
            medicine_data_record['error_found'].append('medcine_composition not in order')
        else:
            medicine_data_record['error_found'] = []
            medicine_data_record['error_found'].append('medcine_composition not in order')

    medicine_data_record_copy = medicine_data_record.copy() #dictionary copy into list addition
    medicine_records.append(medicine_data_record_copy)  #copying the dict to global list




website_url= "https://pharmeasy.in/online-medicine-order/browse"
website_alphabet_url = website_url + "?alphabet="
medicine_urls= []

#for i in list(string.ascii_lowercase):
#     current_url = website_alphabet_url + i + "&page="
#     medicine_urls.append(find_all_medicine_urls(current_url))

current_url = website_alphabet_url + 'a' + "&page="
medicine_urls.extend(find_all_medicine_urls(current_url))
print("url found")

with concurrent.futures.ThreadPoolExecutor(max_workers=12) as executor:
    futures= []
    for url in medicine_urls:
        futures.append(executor.submit(get_medicine_record, url))

mongo_insert_multi_thread(medicine_records)
print(len(medicne_records))
