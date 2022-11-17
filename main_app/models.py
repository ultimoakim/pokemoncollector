from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    can_evolve = models.BooleanField()
    evolution_stage = models.IntegerField()

    def __str__(self):
        return f"Name: {self.name}, Type: {self.type}, Can Evolve: {self.can_evolve}, Evolution Stage: {self.evolution_stage}"