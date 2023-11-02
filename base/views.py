from django.shortcuts import render
from django.http import HttpResponse
from .messenger import Messenger
import requests
import json

# from ..messenger import Messenger
# Create your views here.

def tratar_fone(phone_number):
    formatted_phone_number = f"55{phone_number[0:2]}{phone_number[3:]}" if len(phone_number) >= 3 else phone_number
    return formatted_phone_number

def home(request):
    response_buyers = requests.get('https://trattoria-three.vercel.app/get', json={"sql" : "select * from compradores;"})
    response_data1 = json.loads(response_buyers.content.decode('utf-8'))  # Decodifica os bytes e converte para JSON

    response_tickets = requests.get('https://trattoria-three.vercel.app/get', json={"sql" : "select * from ingressos;"})
    response_data2 = json.loads(response_tickets.content.decode('utf-8'))

    if request.method == 'POST':
        api_key = 'eF4JBUQJX6zG'
        api_url = 'https://trattoria-three.vercel.app/get'
        messenger = Messenger(api_key, api_url)
        
        buyer_id = request.POST.get('buyer_id')

        if 'confirmation_message' in request.POST:
            phone_number = request.POST['phone_number']
            buyer_name = request.POST['buyer_name']
            buyer_id = request.POST.get('buyer_id')
            ingressos = ""

            for value in response_data2['json']:        
                if int(value[6]) == int(buyer_id): 
                    if value[5] == "adult":
                            ingressos = ingressos + "Ingresso: Prato Adulto"
                            if len(value[3]) > 0:
                                 ingressos = ingressos + " - Com Restrição: " + value[3] + "\n\n"
                            else:
                                 ingressos = ingressos + " - Sem Restrição\n\n" 
                    elif value[5] == "kid":
                            ingressos = ingressos + "Ingresso: Prato Criança"
                            if len(value[3]) > 0:
                                 ingressos = ingressos + " - Com Restrição: " + value[3] + "\n\n"
                            else:
                                 ingressos = ingressos + " - Sem Restrição\n\n"
                    elif value[5] == "baby":
                            ingressos = ingressos + "Ingresso: Prato Bebê"
                            if len(value[3]) > 0:
                                 ingressos = ingressos + " - Com Restrição: " + value[3] + "\n\n"
                            else:
                                 ingressos = ingressos + " - Sem Restrição\n\n"

            messenger.send_confirmation_message(tratar_fone(phone_number), buyer_name, ingressos)
            return HttpResponse(f"Mensagem de Confirmação de Pagamento enviada com sucesso! Para comprador {buyer_name} , {phone_number}")

        if 'reminder_message' in request.POST:
            phone_numbers, buyer_names = messenger.fetch_data_from_api()
            for i in range(len(phone_numbers)):
                messenger.send_reminder_message(tratar_fone(phone_numbers[i]), buyer_names[i])
            
            return HttpResponse("Lembretes enviados com sucesso!")

        if 'satisfaction_survey_message' in request.POST:
            phone_numbers, _ = messenger.fetch_data_from_api()
            for phone_number in phone_numbers:
                messenger.send_satisfaction_survey_message(tratar_fone(phone_number))
            return HttpResponse("Pesquisas de Satisfação enviadas com sucesso!")

    context = {'response_buyers': response_data1['json'], 'response_tickets': response_data2['json']}  # Usando a chave principal 'json'
    return render(request, 'base/index.html', context)
