# Generated by Django 4.1.5 on 2023-01-30 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='genre',
            new_name='Género',
        ),
        migrations.AlterField(
            model_name='genero',
            name='genre',
            field=models.CharField(max_length=30, verbose_name='Género'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.IntegerField(blank=True, null=True, verbose_name='Año'),
        ),
    ]
