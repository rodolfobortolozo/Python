# -*- coding: utf-8 -*-
"""
Spyder Editor

lista relação de arquivos na página de dados públicos da receita federal
"""

url = 'https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/cadastros/consultas/dados-publicos-cnpj'
url = 'http://200.152.38.155/CNPJ/'
from bs4 import BeautifulSoup, SoupStrainer
import requests


page = requests.get(url)    
data = page.text
soup = BeautifulSoup(data)


for link in soup.find_all('a'):
    if str(link.get('href')).endswith('.zip'): 
        cam = link.get('href')
        # if cam.startswith('http://http'):
        #     cam = 'http://' + cam[len('http://http//'):] 
        if not cam.startswith('http'):
            print(url+cam)
        else:
            print(cam)
        
