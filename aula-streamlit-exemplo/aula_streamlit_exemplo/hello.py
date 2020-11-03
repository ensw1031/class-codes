import streamlit as st
from bs4 import BeautifulSoup
import requests
import time
import urllib3

requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
try:
    requests.packages.urllib3.contrib.pyopenssl.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
except AttributeError:
    # no pyopenssl support used / needed / available
    pass

st.title('Yet Another Web Scrapper')


#variaveis importantes
apts = []

base_url = st.sidebar.text_input('URL', 'https://www.raulfulgencio.com.br')

max_pages = st.sidebar.slider('Quantas paginas?', 1, 20, 2)

# def get_info(apt):
#     price = apt.find('div', class_='price').find('span').text.strip()
#     title = apt.find('div', class_='info').find('h3').find('a').text.strip()
#     neighborhood = apt.find('div', class_='info').find('h3').find('small').text.strip()
#     detail_url = apt.find('a').get('href')

#     print(f"GET {base_url}/{detail_url}")
#     page = requests.get(f"{base_url}/{detail_url}")
#     soup = BeautifulSoup(page.content, 'html.parser')
#     amenities = soup.find_all('ul', class_='property-amenities-list col-md-6')
#     apt = {
#         'price': price,
#         'title': title,
#         'neighborhood': neighborhood,
#     }

#     info_dict = dict()
#     for col in amenities:
#         infos = col.find_all('li')
#         for info in infos:
#             tokens = info.text.split(':')
#             key = tokens[0].strip().lower()
#             value = tokens[1].strip()
#             info_dict[key] = value
#         # print(f"{key}: {value}")

#     if('suítes' not in info_dict):
#         info_dict['suítes'] = 0

#     if('iptu' not in info_dict):
#         info_dict['iptu'] = 0

#     if('vagas na garagem' not in info_dict):
#         info_dict['vagas na garagem'] = 0

#     apt['info'] = info_dict

#     return apt

x = range(1, max_pages)
# for n in x: 
#     url = f"{base_url}/alugar/Londrina/Apartamento/Padrao/?pag={n}"
#     st.write(f"GET {url}")
#     page = requests.get(url, verify=False)
#     soup = BeautifulSoup(page.content, 'html.parser')
#     apes = soup.find_all('div', class_='item col-sm-6 col-md-4 col-lg-3')
#     percent_completed = 0
#     my_bar = st.progress(percent_completed)
#     count = st.write(f"{percent_completed}")
#     for ape in apes:
#         price = ape.find('div', class_='price').find('span').text.strip()
#         # if('Consulte' not in price):    
#         #     # extract_apt = extract_apt_info(ape)
#         #     # print(extract_apt)
#         #     apts.append(extract_apt)
#         percent_completed = percent_completed + 1
#         my_bar.progress(percent_completed / len(apes))        
#         time.sleep(2)

st.success('Finalizou!')