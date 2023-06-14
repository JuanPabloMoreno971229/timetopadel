from django.db import models
from core.models import torneo

# Create your models here.

OPCIONES = (
    ('Masculino', 'Masculino'),
    ('Femenino', 'Femenino'),
    ('Mixto', 'Mixto'),
)
NIVEL = (
    ('Libre', 'Libre'),
    ('Tercera', 'Tercera'),
    ('Cuarta', 'Cuarta'),
    ('Mixtos', 'Mixtos'),
)
class inscripcion(models.Model):

    tournament = models.ForeignKey(torneo, on_delete=models.CASCADE, verbose_name="Torneo")
    name_1 = models.CharField(max_length=500, null=False, verbose_name= "Nombre jugador 1")
    lastname_1 = models.CharField(max_length=500, null=False, verbose_name= "Apellido jugador 1")
    phone_1 = models.IntegerField( null=False, verbose_name= "Teléfono jugador 1")
    mail_1 = models.EmailField(max_length=500, null=False, verbose_name= "Correo jugador 1")
    name_2 = models.CharField(max_length=500, null=False, verbose_name= "Nombre jugador 2")
    lastname_2 = models.CharField(max_length=500, null=False, verbose_name= "Apellido jugador 2")
    phone_2 = models.IntegerField( null=False, verbose_name= "Teléfono jugador 2")
    mail_2 = models.EmailField(max_length=500, null=False, verbose_name= "Correo jugador 2")
    category = models.CharField(max_length=200, null=True, verbose_name="Categoria", choices=OPCIONES)
    level = models.CharField(max_length=200, null=True, verbose_name="Nivel", choices=NIVEL)
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated= models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Inscripción"
        verbose_name_plural = "Inscripciones"
        ordering = ["-created"]
                
    def __str__(self):
        return f"{self.name_1} and {self.name_2}"