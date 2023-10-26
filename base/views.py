from django.shortcuts import render
import requests
# Create your views here.

def home(request):
    response = requests.get('https://trattoria-three.vercel.app/get', json={"sql" : "select * from compradores;"})
    context = {'response' : response}
    return render(request, 'base/index.html', context)