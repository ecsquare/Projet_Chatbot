from django.shortcuts import render

# pour page d'acueil
def accueil(request):
	context = {}
	return render(request ,'chatbot_tutorial/index.html', context )


