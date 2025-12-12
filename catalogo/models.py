from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='productos')
    # Puedes guardar aquí una URL o el nombre del archivo en /static/
    imagen = models.URLField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()  # permite descripciones largas
    stock = models.PositiveIntegerField(default=0) 
    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
