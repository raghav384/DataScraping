import requests
from bs4 import BeautifulSoup
import string
import pickle



def find_medicine_for_alphabet(current_url):
    print(current_url)
    url = current_url + '0'
    output_response = requests.get(url)
    #print(output_response)
    
    soup = BeautifulSoup(output_response.content,'html.parser')
    output = soup.findAll("div",{"class":"U9o7k"})
    name_list = []
    for i in range(len(output)):
        name_list.append(output[i].a.text)
    
    page_number = soup.findAll("div",{"class":"_1FJiY"})
    page_number_text = page_number[0].span.text
    page_val = int(page_number_text.split("/")[1])
    #print(page_val)
    for i in range(1,page_val):
        url = current_url + str(i)
        output_response = requests.get(url)
        soup = BeautifulSoup(output_response.content,'html.parser')
        output1 = soup.findAll("div",{"class":"U9o7k"})
        for i in range(len(output1)):
            name_list.append(output1[i].a.text)
   
    #print(name_list)    
    return name_list






base_url_medicine_names = "https://pharmeasy.in/online-medicine-order/browse"
alphabhet_url = base_url_medicine_names + "?alphabet="



name_wise_medicines = {}
for i in list(string.ascii_lowercase):
    current_url = alphabhet_url + i + "&page="
    name_wise_medicines[i] = find_medicine_for_alphabet(current_url)
    
    
filename = 'list_data'
outfile = open(filename,'wb')
pickle.dump(name_wise_medicines,outfile)
outfile.close()    

