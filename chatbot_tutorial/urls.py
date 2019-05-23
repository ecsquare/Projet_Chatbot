from django.conf.urls import url,include
from django.contrib import admin
from .views import chat
from .chatbotmanager import ChatbotManager
from chatbot_tutorial.core import views as core_views
from django.contrib.auth import views as auth_views


urlpatterns = [

	url(r'^chat/', chat, name='chat'),
	url(r'^$',include('chatbot_tutorial.debut.urls')),
	url(r'^feedback/$',include('chatbot_tutorial.form.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^next', core_views.home, name='home'),

]
