import os
import requests
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('API_DNI_TOKEN')

def verificar_DNI(dni):
   url = "https://api.apis.net.pe/v2/reniec/dni?numero={0}&token={1}".format(dni, API_KEY)
   response = requests.get(url)
   return response.json()