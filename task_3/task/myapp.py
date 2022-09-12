import requests
import json

URL ="http://127.0.0.1:8000/user/"

data ={
    'user': 'anmol',
    'email':'anmol12@gmail.com',
    'state':'up',
    'district':'bareilly'
}
json_data = json.dumps(data)
r = requests.post(url = URL, data = json_data)
data = r.json()
print(data)