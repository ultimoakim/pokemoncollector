from django.db import models
from django.urls import reverse

# Field.choices
ELEMENTS = (
    ('NOR', 'Normal'),
    ('FIR', 'Fire'),
    ('WAT', 'Water'),
    ('ELE', 'Electric'),
    ('GRA', 'Grass'),
    ('ICE', 'Ice'),
    ('FIG', 'Fighting'),
    ('POI', 'Poison'),
    ('GRO', 'Ground'),
    ('FLY', 'Flying'),
    ('BUG', 'Bug'),
    ('ROC', 'Rock'),
    ('GHO', 'Ghost'),
    ('DRA', 'Dragon'),
    ('DAR', 'Dark'),
    ('STE', 'Steel'),
    ('FAI', 'Fairy'),
)

# Create your models here.
class Weakness(models.Model):
    element = models.CharField(max_length = 15)

    def __str__(self):
        return self.element
    
    def get_absolute_url(self):
        return reverse('weaknesses_detail', kwargs={'pk': self.id})

class Pokemon(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    can_evolve = models.BooleanField()
    evolution_stage = models.IntegerField()
    # Creating a M:M relationship with Weakness
    weaknesses = models.ManyToManyField(Weakness)

    def __str__(self):
        return f"Name: {self.name}, Type: {self.type}, Can Evolve: {self.can_evolve}, Evolution Stage: {self.evolution_stage}"

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pokem_id': self.id})

class Move(models.Model):
    movename = models.CharField('Move Name', max_length=25)
    element = models.CharField(
        max_length=20,
        choices=ELEMENTS,
        default=ELEMENTS[0][0],
    )
    pokemon = models.ForeignKey('Pokemon', on_delete=models.CASCADE)

    def __str__(self):
        return f"Move Name: {self.movename}, Element: {self.get_element_display()}"

