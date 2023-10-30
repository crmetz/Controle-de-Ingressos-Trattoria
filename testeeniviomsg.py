import requests
import time

PHONE_NUMBER = ['555499007422', '555497052042', '555491719907', '555491407557']
API_KEY = 'eF4JBUQJX6zG'

message = 'teste mensagem api quem leu e viado'


for number in PHONE_NUMBER:
    time.sleep(5)
    requests.get(
        url=f'http://api.textmebot.com/send.php?recipient=+{number}&apikey={API_KEY}&text={message}'
    )



