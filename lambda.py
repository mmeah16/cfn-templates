import requests
import os 
from dotenv import load_dotenv

load_dotenv()

url = os.getenv('LAMBDA_ENDPOINT')

payload = {}
headers = {}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
