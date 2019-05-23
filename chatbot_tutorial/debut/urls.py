from django.conf.urls import url
from .views import accueil 

urlpatterns = [
	
	url(r'', accueil, name='accueil'),
]
