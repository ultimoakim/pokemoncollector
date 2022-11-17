from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pokemon/', views.pokemon_index, name='index'),
    # Details for a Pokemon's page RESTful routing: /pokemon/:id
    # However, do NOT forget that Django has the trailing slash at the end. They also do NOT start with slashes like in Express.
    # You can call the id variable whatever you want. However, keep in mind that this is the variable that you will use in your pokemon_detail function in views.py! We're gonna set it to poke_id, but you can set it to tuna_id! Literally any name you want. So yes, this is separate from our template variable poke. Please don't forget that.
    path('pokemon/<int:pokem_id>/', views.pokemon_detail, name='detail'),
]