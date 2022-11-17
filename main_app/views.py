from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Importing the Pokemon model here:
from .models import Pokemon

# Create your views here.

def home(request):
    # In Django, we include .html file extensions, unlike rendering .ejs templates. See how the format is different?
    # All view (controller, if it was Express) functions need to define a positional parameter to accept the request object that Django will be passing in. This request object is very much like the req object in Express functions.
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def pokemon_index(request):
    # What we're doing here is passing data to a template, very much like we did in Express!
    pokemon = Pokemon.objects.all()
    return render(request, 'pokemon/index.html', {
        'pokemon': pokemon
    })

# Something important to remember: In urls.py, if you have ANY ROUTE PARAMETERS, ANY URL params that you've defined, they will be passed in as additional arguments when the view function is called. So we need to define ADDITIONAL PARAMETERS TO ACCEPT THOSE ADDITIONAL ARGUMENTS! And what would that be? The URL ID THAT WE PUT IN urls.py!
def pokemon_detail(request, pokem_id):
    pokemon = Pokemon.objects.get(id=pokem_id)
    return render(request, 'pokemon/detail.html', {'pocketmonsters': pokemon})

class PokemonCreate(CreateView):
    model = Pokemon
    fields = '__all__'



