import requests

from time import sleep

url = "http://localhost:4444/predict"

client = {"job": "management", "duration": 400, "poutcome": "success"}

while True:
    #sleep(0.1)
    #sleep(0.01)
    response = requests.post(url, json=client).json()
    print(response)
