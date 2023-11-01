import requests

# response = requests.get(url='https://trattoria-ochre.vercel.app/get', json={'sql':"select * from teste;"})

# table = response.json()

# print(table['json'])

response = requests.get('https://trattoria-three.vercel.app/get', json={"sql" : "select * from compradores;"})
#
#response = requests.post('https://trattoria-three.vercel.app/post', json={"sql" : "INSERT INTO ingressos()VALUES (57, 'Cristian Metz', '03855254087', 'Intolerância à lactose', 'Ninguem', 'adult', 57);"})

#response = requests.post('https://trattoria-three.vercel.app/post', json={'sql':"INSERT INTO compradores VALUES (43, 'Miguel Valentini ', '5499007422', '03855254087', 'teste@gmail.com', 'nao-pago', 0);"})


print(response.text)