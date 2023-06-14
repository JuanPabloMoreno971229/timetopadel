from django.db import models
from django.contrib.admin.widgets import AdminTimeWidget
# Create your models here.

OPCIONES = (
    ('Libre', 'Libre'),
    ('Tercera', 'Tercera'),
    ('Cuarta', 'Cuarta'),
    ('Mixtos', 'Mixtos'),
)

class club(models.Model):

    name = models.CharField(max_length=200, null=False,verbose_name="Nombre del club")
    address = models.CharField(max_length=200, verbose_name="Dirección")
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated= models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Club"
        verbose_name_plural = "Clubs"
        ordering = ["-created"]
                
    def __str__(self):
        return self.name



class torneo(models.Model):

    name = models.CharField(max_length=500, null=False, verbose_name= "Nombre del torneo")
    start_date = models.DateField(verbose_name="Fecha de inicio")
    end_date = models.DateField(verbose_name="Fecha de fin")
    hour = models.TimeField(verbose_name="Hora de inicio")
    price = models.FloatField(verbose_name="Precio")
    place = models.ForeignKey(club, verbose_name="Lugar", on_delete=models.CASCADE)
    category = models.CharField(max_length=200, null=True, verbose_name="Categoria", choices=OPCIONES)
    image = models.ImageField(null=True, upload_to='imagen torneo', verbose_name="Imagen")
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated= models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Torneo"
        verbose_name_plural = "Torneos"
        ordering = ["-created"]
                
    def __str__(self):
        return self.name




