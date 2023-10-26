import requests

PHONE_NUMBER = ['555497052042', '555499007422', '555499107432', '555499407433']
API_KEY = 'DktYVcpVUMap'

compradores = ['henrique', 'cristian', 'mauricio', 'vinicius']



for i in range(PHONE_NUMBER):
    message = f'''Olá, {compradores[i]}, gostaríamos de agradecer pela compra do ingresso para a Trattoria! Ficamos felizes de recebê-lo em nossa experiência gastronômica, que foi pensada com muito carinho para vocês.

    Gostaríamos também de confirmar os ingressos:

    ingresso - prato normal

    ingresso - prato infantil'''

    requests.get(
    url=f'http://api.textmebot.com/send.php?recipient=+{PHONE_NUMBER[i]}&apikey={API_KEY}&text={message}'
    )