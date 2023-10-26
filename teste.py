import requests

# response = requests.get(url='https://trattoria-ochre.vercel.app/get', json={'sql':"select * from teste;"})

# table = response.json()

# print(table['json'])

response = requests.get('https://trattoria-three.vercel.app/get', json={"sql" : "select * from ingressos;"})
#
#  response = requests.post('https://trattoria-three.vercel.app/post', json={"sql" : ""})

print(response.text)