import requests
import json
import time

class Messenger:
    def __init__(self, api_key, api_url):
        self.api_key = api_key
        self.api_url = api_url

    def fetch_data_from_api(self):
        try:
            response = requests.get(self.api_url, json={"sql": "select * from compradores;"})
            response.raise_for_status()  # Verifica se houve erro na requisição
            response_data = json.loads(response.content.decode('utf-8'))
            
            phone_numbers = [item[2] for item in response_data['json']]  # O índice 2 é para o campo "Telefone"
            buyer_names = [item[1] for item in response_data['json']]
            

            return phone_numbers, buyer_names
        except (requests.RequestException, requests.HTTPError, ValueError) as e:
            print(f"Erro ao obter dados da API: {e}")
            return [], []

    def send_confirmation_message(self, phone_number, buyer_name, ingressos):
        message = f'''Olá👋, {buyer_name}! \n\nGostaríamos de agradecer pela compra do ingresso para a Trattoria! Ficamos felizes em recebê-lo(a) na nossa experiência gastronômica, que foi pensada com muito carinho para vocês.🍝🍴🇮🇹 \n\nGostaríamos também de confirmar os ingressos: \n{ingressos} '''
        self._send_message(phone_number, message)

    def send_reminder_message(self, phone_number, buyer_name):
        message = f'''Olá, {buyer_name}!\n\nTudo bem? Estamos empolgados com a proximidade do evento Trattoria Arte Italiana 🍝, elaborado com carinho pelos alunos dos cursos técnicos do CETEC UCS. Segue as informações necessárias para seu comparecimento no evento:\n\n📅Data: 09/11/2023\n⏰Início: 19:00\n📌Endereço: Av. Vindima, nº 1000, Parque de Eventos Eloy Kunz, Flores da Cunha, RS.\n\nSerá um prazer imenso contar com a sua presença! Até lá!'''

        self._send_message(phone_number, message)

    def send_satisfaction_survey_message(self, phone_number):
        message = '''Caros Clientes:\n\nA Trattoria chegou ao fim! Planejar este evento tão importante não foi uma tarefa fácil, mas com certeza foi satisfatória. Agradecemos a sua presença e esperamos que você tenha gostado! Gostaríamos de saber sua opinião sobre a noite! Abraços do Técnico em Administração, Gastronomia e Informática 😊. \n\nSegue o link para a pesquisa: \nhttps://docs.google.com/forms/d/e/1FAIpQLSfkzm6_XXUK60531KK0f8qHqqIcBHuZmcKQ4VD8BAhfwAZ5FA/viewform?pli=1'''
        self._send_message(phone_number, message)

    def _send_message(self, phone_number, message):
        try:
            response = requests.get(
                url=f'http://api.textmebot.com/send.php?recipient=+{phone_number}&apikey={self.api_key}&text={message}'
            )
            response.raise_for_status()  # Verifica se houve erro na requisição
            print(f"Mensagem enviada para {phone_number}.")
            time.sleep(5)
        except requests.RequestException as e:
            print(f"Erro ao enviar mensagem para {phone_number}: {e}")

if __name__ == "__main__":
    API_KEY = 'eF4JBUQJX6zG'
    API_URL = 'https://trattoria-three.vercel.app/get'

    messenger = Messenger(API_KEY, API_URL)

    # Obtendo dados dos compradores
    phone_numbers, buyer_names = messenger.fetch_data_from_api()

    # Enviando as mensagens para os compradores usando os dados obtidos
    for i in range(len(phone_numbers)):
        messenger.send_confirmation_message(phone_numbers[i], buyer_names[i])
        messenger.send_reminder_message(phone_numbers[i], buyer_names[i])

    # Envio da pesquisa de satisfação após o evento para todos os compradores
    for phone_number in phone_numbers:
        messenger.send_satisfaction_survey_message(phone_number)



















































# import requests
# import json

# class Messenger:
#     def __init__(self, api_key):
#         self.api_key = api_key\

#     def fetch_data_from_api(self, api_url):
#         response = requests.get(api_url, json={"sql": "select * from compradores;"})
#         response_data = json.loads(response.content.decode('utf-8'))
#         phone_numbers = [item[2] for item in response_data['json']]  # O índice 2 é para o campo "Telefone"
#         buyer_names = [item[1] for item in response_data['json']]  # O índice 1 é para o campo "Nome"
#         return phone_numbers, buyer_names

#     def send_message(self, phone_number, buyer_name, message):
#         message = f'''Olá, {buyer_name}, gostaríamos de agradecer pela compra do ingresso para a Trattoria! Ficamos felizes de recebê-lo em nossa experiência gastronômica, que foi pensada com muito carinho para vocês.

#         Gostaríamos também de confirmar os ingressos:

#         ingresso - prato normal

#         ingresso - prato infantil'''

#         requests.get(
#             url=f'http://api.textmebot.com/send.php?recipient=+{phone_number}&apikey={self.api_key}&text={message}'
#         )

# if __name__ == "__main__":
#     API_KEY = 'DktYVcpVUMap'
#     API_URL = 'https://trattoria-three.vercel.app/get'

#     messenger = Messenger(API_KEY)
#     phone_numbers, buyer_names = messenger.fetch_data_from_api(API_URL)

#     for i in range(len(phone_numbers)):
#         messenger.send_message(phone_numbers[i], buyer_names[i])