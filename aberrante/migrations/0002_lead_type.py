# Generated by Django 4.2.16 on 2025-02-06 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aberrante', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='type',
            field=models.CharField(blank=True, choices=[('collector', 'Coleccionista'), ('artist', 'Artista'), ('other', 'Otro')], default='other', max_length=20),
        ),
    ]
