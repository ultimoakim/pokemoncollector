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
    # Creating Pokemon: pokemon/create/
    path('pokemon/create/', views.PokemonCreate.as_view(), name='pokemon_create'),
    # Updating Pokemon: pokemon/<int:pk>/update/. Remember, now we're using CLASS-BASED VIEWS, so any time we need the id, we're gonna put in pk. You MUST put in pk for class-based views!
    path('pokemon/<int:pk>/update/', views.PokemonUpdate.as_view(), name='pokemon_update'),
    # Deleting Pokemon: pokemon/<int:pk>/delete/
    path('pokemon/<int:pk>/delete/', views.PokemonDelete.as_view(), name='pokemon_delete'),
    path('pokemon/<int:pokem_id>/add_move/', views.add_move, name='add_move'),
    # Now then, we add our routes for our weaknesses model!
    path('pokemon/<int:pokem_id>/assoc_weakness/<int:weakness_id>/', views.assoc_weakness, name='assoc_weakness'),
    path('pokemon/<int:pokem_id>/unassoc_weakness/<int:weakness_id>/', views.unassoc_weakness, name='unassoc_weakness'),
    path('weaknesses/', views.WeaknessList.as_view(), name='weaknesses_index'),
    path('weaknesses/<int:pk>/', views.WeaknessDetail.as_view(), name='weaknesses_detail'),
    path('weaknesses/create/', views.WeaknessCreate.as_view(), name='weaknesses_create'),
    path('weaknesses/<int:pk>/update/', views.WeaknessUpdate.as_view(), name='weaknesses_update'),
    path('weaknesses/<int:pk>/delete/', views.WeaknessDelete.as_view(), name='weaknesses_delete'),
]