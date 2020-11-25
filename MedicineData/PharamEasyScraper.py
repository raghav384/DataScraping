import requests
from bs4 import BeautifulSoup
from database_functions import  mongo_insert
import string


def find_medicine_for_alphabet(current_url):
    print(current_url)
    url = current_url + '0'

    output_response = requests.get(url)     # only tranversing the page 0 for now
    soup = BeautifulSoup(output_response.content,'html.parser')
    output = soup.findAll("div",{"class":"U9o7k"})

    name_list = []
    for i in range(len(output)):
        print(i)
        medicine_data_record = {}
        medicine_url = "https://pharmeasy.in" +  str(output[i].a['href'])
        medicine_response = requests.get(medicine_url)
        medicine_data_soup = BeautifulSoup(medicine_response.content,'html.parser')
        try:
            medicine_data_record['medicine_name'] = medicine_data_soup.find("h1",{"class":"ooufh"}).text
        except:
            medicine_data_record['medicine_name'] = medicine_data_soup.find("h1",{"class":"ooufh"})
            medicine_data_record['error_found'] = []
            medicine_data_record['error_found'].append('medcine_name not in order')
        try:
            medicine_data_record['medicine_producer'] = medicine_data_soup.find("div",{"class":"_3JVGI"}).text
        except:
            medicine_data_record['medicine_producer'] = medicine_data_soup.find("div",{"class":"_3JVGI"})
            if 'error_found' in medicine_data_record.keys():
                medicine_data_record['error_found'].append('medcine_producer not in order')
            else:
                medicine_data_record['error_found'] = []
                medicine_data_record['error_found'].append('medcine_producer not in order')

        try:
            medicine_data_record['medicine_number_of_strips'] = int(medicine_data_soup.find("div",{"class":"_36aef"}).text.split(" ")[0])
        except:
            medicine_data_record['medicine_number_of_strips'] = medicine_data_soup.find("div",{"class":"_36aef"})
            if 'error_found' in medicine_data_record.keys():
                medicine_data_record['error_found'].append('medcine_strip not in order')
            else:
                medicine_data_record['error_found'] = []
                medicine_data_record['error_found'].append('medcine_strip not in order')
        try:
            medicine_data_record['medicine_price'] = medicine_data_soup.find("div",{"class":"_1_yM9"}).text
        except:
            medicine_data_record['medicine_price'] = medicine_data_soup.find("div",{"class":"_1_yM9"})
            if 'error_found' in medicine_data_record.keys():
                medicine_data_record['error_found'].append('medcine_price not in order')
            else:
                medicine_data_record['error_found'] = []
                medicine_data_record['error_found'].append('medcine_price not in order')

        try:
            medicine_data_record['medicine_vendor_price'] =  float(medicine_data_soup.find("div",{"class":"_3FUtb"}).text.split("₹")[1])
        except:
            medicine_data_record['medicine_vendor_price'] =  medicine_data_soup.find("div",{"class":"_3FUtb"})
            if 'error_found' in medicine_data_record.keys():
                medicine_data_record['error_found'].append('medcine_vendor_price not in order')
            else:
                medicine_data_record['error_found'] = []
                medicine_data_record['error_found'].append('medcine_vendor_price not in order')

        try:
            medicine_data_record['medicine_dicount'] = float(medicine_data_soup.find("div",{"class":"_306Fp"}).text.split("%")[0])
        except:
            medicine_data_record['medicine_dicount'] = medicine_data_soup.find("div",{"class":"_306Fp"})
            if 'error_found' in medicine_data_record.keys():
                medicine_data_record['error_found'].append('medcine_discount not in order')
            else:
                medicine_data_record['error_found'] = []
                medicine_data_record['error_found'].append('medcine_discount not in order')
        try:
            medicine_data_record['medicine_composition'] = medicine_data_soup.find("div",{"class":"_3Phld"}).text
        except:
            medicine_data_record['medicine_composition'] = medicine_data_soup.find("div",{"class":"_3Phld"})
            if 'error_found' in medicine_data_record.keys():
                medicine_data_record['error_found'].append('medcine_composition not in order')
            else:
                medicine_data_record['error_found'] = []
                medicine_data_record['error_found'].append('medcine_composition not in order')

        try:
            medicine_data_record['medicine_theuraptic_Classification'] = medicine_data_soup.find("td",{"class":"_3C_XR"}).text
        except:
            medicine_data_record['medicine_theuraptic_Classification'] = medicine_data_soup.find("td",{"class":"_3C_XR"})
            if 'error_found' in medicine_data_record.keys():
                medicine_data_record['error_found'].append('medcine_composition not in order')
            else:
                medicine_data_record['error_found'] = []
                medicine_data_record['error_found'].append('medcine_composition not in order')

        name_list.append(medicine_data_record)
    return name_list


base_url_medicine_names = "https://pharmeasy.in/online-medicine-order/browse"
alphabhet_url = base_url_medicine_names + "?alphabet="
alphabet_wise_medicines = {}


#for i in list(string.ascii_lowercase):
#    current_url = alphabhet_url + i + "&page="
#    alphabet_wise_medicines[i] = find_medicine_for_alphabet(current_url)

current_url = alphabhet_url + 'a' + "&page="
alphabet_wise_medicines[i] = find_medicine_for_alphabet(current_url)
print("Success")
mongo_insert(alphabet_wise_medicines)
