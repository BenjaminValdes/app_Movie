from django.db import models


class Genero(models.Model):
    genre = models.CharField('Género', max_length=30)

    def __str__(self):
        return f'{self.genre}'


class Movie(models.Model):
    REVIEW = (
        ('A', 'Excelente'),
        ('B', 'Buena'),
        ('C', 'Regular'),
        ('D', 'Mala'),
        ('E', 'Muy mala')
    )
    name = models.CharField('Nombre', max_length=50)
    Género = models.ForeignKey(Genero, on_delete=models.CASCADE,
                                null=True, blank=True)
    year = models.IntegerField('Año', null=True, blank=True)
    review = models.CharField('Valoración', max_length=4, choices=REVIEW, default='C')
    date_create = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

#Evita que se creen dos películas iguales
    class Meta:
        unique_together = ['name']

#Identifica si se está creando una película nueva o se está modificando
    def save(self, *args, **kwargs):
        if self.id is None:
            self.name = f'{self.name}'
        super(Movie, self).save(*args, **kwargs)


    def __str__(self):
        return f'{self.name}  -  {self.Género}  -  {self.year}'


