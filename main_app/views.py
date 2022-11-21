from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Importing the Pokemon model here:
from .models import Pokemon
from .forms import MoveForm

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
# That's why I did pokem_id on purpose in urls.py just to prove a point that the parameter we put inside of our function here is the URL ID that we put in urls.py. In the path('pokemon/<int:pokem_id>/', views.pokemon_detail, name='detail').
def pokemon_detail(request, pokem_id):
    pokemon = Pokemon.objects.get(id=pokem_id)
    move_form = MoveForm()
    return render(request, 'pokemon/detail.html', {
        'pocketmonsters': pokemon,
        'move_form': move_form
    })

# This is being put on the details.html page.
def add_move(request, pokem_id):
    form = MoveForm(request.POST)
    if form.is_valid():
        new_move = form.save(commit=False)
        new_move.pokemon_id = pokem_id
        new_move.save()
    return redirect('detail', pokem_id=pokem_id)

class PokemonCreate(CreateView):
    model = Pokemon
    fields = '__all__'

class PokemonUpdate(UpdateView):
    model = Pokemon
    fields = ['type', 'can_evolve', 'evolution_stage']

class PokemonDelete(DeleteView):
    model = Pokemon
    success_url = '/pokemon'
    # Again, this is the same thing as redirect, which means you would write the path of the URL! And that means STARTING with a forward slash, like in Express!



