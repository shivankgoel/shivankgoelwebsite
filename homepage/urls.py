from django.urls import path
from homepage import views

urlpatterns = [
	path('academic/', views.academic, name='academic'),
	path('experience/', views.experience, name='experience'),
	path('publicspeaking/', views.publicspeaking, name='publicspeaking'),
	path('tech_pe_charcha/', views.tech_pe_charcha, name='tech_pe_charcha'),
	path('contact/', views.contact, name='contact'),
	path('reading/', views.reading, name='reading'),
	path('', views.index, name ='index'),
]
