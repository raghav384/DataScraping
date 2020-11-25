import requests
from bs4 import BeautifulSoup
import string
import pickle

def find_medicine_for_alphabet(current_url):
    print(current_url)
    url = current_url + '0'
    output_response = requests.get(url)
    soup = BeautifulSoup(output_response.content,'html.parser')
    output = soup.findAll("div",{"class":"U9o7k"})
    name_list = []
    #for i in range(len(output)):
    #    name_list.append(output[i].a['href'])

    #Class for medicine information retrieval : _3bwoY
    medicine_url = "https://pharmeasy.in/online-medicine-order" +  output[0].a['href']
    medicine_response = requests.get(medicine_url)
    medicine_data_soup = BeautifulSoup(medicine_response.content,'html.parser')


    print(medicine_data_soup.findAll("div",{"class":"_2UHQK"})[0].h1.text)



    title=  medicine_data_soup.findAll("h1",{"class":"ooufh"})
    comp_name=   medicine_data_soup.find(class_="_3JVGI").string
    NO_of_strips=  medicine_data_soup.find(class_="_36aef").string
    Vendor_Price=  medicine_data_soup.find(class_="_1_yM9").string
    Actual_Price=  medicine_data_soup.find(class_="_3FUtb").string
    Discount=  medicine_data_soup.find(class_="_306Fp").string
    description=  medicine_data_soup.find(class_="_1ZIK6").string
    #edicine_record = {}
    print(tile,comp_name,NO_of_strips,Vendor_Price,Actual_Price,Discount,description)

    print(name_list)
    return name_list

base_url_medicine_names = "https://pharmeasy.in/online-medicine-order/browse"
alphabhet_url = base_url_medicine_names + "?alphabet="
name_wise_medicines = {}

current_url = alphabhet_url + 'a' + "&page="
name_wise_medicines[0] = find_medicine_for_alphabet(current_url)

#for i in list(string.ascii_lowercase):
#    current_url = alphabhet_url + i + "&page="
#    name_wise_medicines[i] = find_medicine_for_alphabet(current_url)
