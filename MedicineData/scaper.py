import requests
from bs4 import BeautifulSoup
from database_functions import  mongo_insert
import string


def find_medicine_for_alphabet(current_url):
    print(current_url)
    url = current_url + '0'
    # only tranversing the page 0 for now 
    output_response = requests.get(url)
    soup = BeautifulSoup(output_response.content,'html.parser')
<<<<<<< HEAD
    output = soup.find_all("div",{"class":"U9o7k"})
    name_list = []
    #for i in range(len(output)):
    #    name_list.append(output[i].a['href'])

    #Class for medicine information retrieval : _3bwoY
    medicine_url = "https://pharmeasy.in/" +  output[0].a['href']
    print(medicine_url)
    medicine_response = requests.get(medicine_url)
    medicine_data_soup = BeautifulSoup(medicine_response.content,'html.parser')
    print(medicine_data_soup.prettify())

    print(medicine_data_soup.findAll('div',{"class":"_3bwoY"}))

=======
    output = soup.findAll("div",{"class":"U9o7k"})
    
    name_list = []
    for i in range(len(output)):
        medicine_data_record = {}
        medicine_url = "https://pharmeasy.in" +  str(output[i].a['href'])
        medicine_response = requests.get(medicine_url)
        medicine_data_soup = BeautifulSoup(medicine_response.content,'html.parser')
        medicine_data_record['medicine_name'] = medicine_data_soup.find("h1",{"class":"ooufh"}).text
        medicine_data_record['medicine_producer'] = medicine_data_soup.find("div",{"class":"_3JVGI"}).text
        medicine_data_record['medicine_number_of_strips'] = int(medicine_data_soup.find("div",{"class":"_36aef"}).text.split(" ")[0])
        medicine_data_record['medicine_price'] = medicine_data_soup.find("div",{"class":"_1_yM9"}).text
        medicine_data_record['medicine_vendor_price'] =  float(medicine_data_soup.find("div",{"class":"_3FUtb"}).text.split("₹")[1])
        medicine_data_record['medicine_dicount'] = float(medicine_data_soup.find("div",{"class":"_306Fp"}).text.split("%")[0])
        medicine_data_record['medicine_composition'] = medicine_data_soup.find("div",{"class":"_3Phld"}).text
        medicine_data_record['medicine_theuraptic_Classification'] = medicine_data_soup.find("td",{"class":"_3C_XR"}).text
        name_list.append(medicine_data_record)
    return name_list
>>>>>>> 5a5aa4111122401a54c1d424a7ec77820e8dcb47




base_url_medicine_names = "https://pharmeasy.in/online-medicine-order/browse"
alphabhet_url = base_url_medicine_names + "?alphabet="
alphabet_wise_medicines = {}


for i in list(string.ascii_lowercase):
    current_url = alphabhet_url + i + "&page="
    alphabet_wise_medicines[i] = find_medicine_for_alphabet(current_url)
print("Success")
mongo_insert(alphabet_wise_medicines)
    
    
