from django.views import generic
from django.views.decorators.csrf import csrf_exempt
import json
import requests
import random
from django.utils.decorators import method_decorator
from django.http.response import HttpResponse
from django.shortcuts import render
from .chatbotmanager import ChatbotManager 
from .models import chatClient

def chat(request):
    context = {}
    return render(request, 'chatbot_tutorial/chatbot.html', context)


def respond_to_websockets(message): 

	
    result_message = {
        'type': 'text'
    }
    if (message['text'] in "Salut"):
    	result_message['text']="Bienvenue! Je suis MrBot. Disponible 24/24 pour vos questions futurs entrepreneurs!"
    elif (message['text'] in "Je veux devenir entrepreneur!"):
    	result_message['text']="Si on veut, on peux!"

    elif (message['text'] in "C'est quoi l'étude du marché?"):
    	result_message['text']="Etape qui permet d’identifier la concurrence et de déterminer la zone de chalandise"
    elif (message['text'] in "Tu es mauvais"):
    	result_message['text']="Je suis professionnel! Je réponds qu'aux questions professionnels"
    elif (message['text'] in "Cv"):
        result_message['text']="Cv bien et vous?"
    elif (message['text'] in "Ca marche"):
        result_message['text']="Vous avez des questions à poser?"
    elif (message['text'] in "Comment trouver une idée de projet?"):
        result_message['text']="C’est en observant son environnement qu’un futur porteur de projet trouvera son idée d’entreprise."
    elif (message['text'] in "Ou trouver l'inspiration?"):
        result_message['text']="La vie quotidienne et la vie économique mondiale sont des sources d’inspiration pour la création d’entreprise"
    elif (message['text'] in "C'est quoi un marché?"):
        result_message['text']="Le marché est l’environnement dans lequel se positionne l’entreprise"
    elif (message['text'] in "Est-il important de faire l'étude du marché?"):
        result_message['text']="L’étude du marché est importante pour définir la stratégie d’une entreprise. "
    elif (message['text'] in "Quels sont les qualités d'un entrepreneur?"):
        result_message['text']="l’indépendance , la créativité et l’innovation, le goût du risque et la prudence"
    elif (message['text'] in "Merci"):
        result_message['text']="Je serai toujours à votre disposition"
   
    else:
    	r= ChatbotManager.callBot(message['text'])
    	result_message['text'] = r
    
    return result_message
    