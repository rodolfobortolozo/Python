# Script desenvolvido para importar as Rotas do Sistema RoadNet para Power Bi
import requests
import json
from requests.structures import CaseInsensitiveDict
import pandas as pd


URL_LOGIN = "https://apex-prod-integration.aws.roadnet.com/integration/v1/login"
URL_ROUTES = "https://apex-prod-integration.aws.roadnet.com/integration/v1/dailyplan/routes"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"

data = """{
    "username": "",
    "password": ""
}"""
response = requests.post(
                         URL_LOGIN,
                         headers=headers,
                         data=data)

if response.status_code == 200:
    ssh_keys = json.loads(response.content.decode('utf-8'))

headers["Authorization"] = "Bearer {}".format(ssh_keys['token'])

response = requests.get(URL_ROUTES, headers=headers)

json = json.loads(response.text)

df_routers = pd.json_normalize(json['items'])

