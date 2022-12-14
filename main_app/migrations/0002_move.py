# Generated by Django 4.1.3 on 2022-11-19 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movename', models.CharField(max_length=25)),
                ('element', models.CharField(choices=[('NOR', 'Normal'), ('FIR', 'Fire'), ('WAT', 'Water'), ('ELE', 'Electric'), ('GRA', 'Grass'), ('ICE', 'Ice'), ('FIG', 'Fighting'), ('POI', 'Poison'), ('GRO', 'Ground'), ('FLY', 'Flying'), ('BUG', 'Bug'), ('ROC', 'Rock'), ('GHO', 'Ghost'), ('DRA', 'Dragon'), ('DAR', 'Dark'), ('STE', 'Steel'), ('FAI', 'Fairy')], default='NOR', max_length=20)),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.pokemon')),
            ],
        ),
    ]
