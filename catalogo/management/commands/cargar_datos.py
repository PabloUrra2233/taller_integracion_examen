from django.core.management.base import BaseCommand
from catalogo.models import Categoria, Producto

class Command(BaseCommand):
    help = 'Carga datos iniciales usando el ORM de Django'

    def handle(self, *args, **kwargs):
        self.stdout.write("Iniciando carga de datos...")

        # 1. Crear Categorias usando get_or_create para evitar duplicados
        cat_libros, _ = Categoria.objects.get_or_create(nombre='Libros')
        cat_papeleria, _ = Categoria.objects.get_or_create(nombre='Papelería')
        cat_tecnologia, _ = Categoria.objects.get_or_create(nombre='Tecnología')

        self.stdout.write("- Categorías verificadas.")

        # 2. Lista de diccionarios con los datos de los productos
        productos_data = [
            {
                'nombre': 'El Principito',
                'categoria': cat_libros,
                'precio': 8990,
                'descripcion': 'Edición clásica tapa blanda.',
                'imagen': ''
            },
            {
                'nombre': 'Cuaderno College',
                'categoria': cat_papeleria,
                'precio': 1500,
                'descripcion': 'Cuaderno cuadriculado 100 hojas.',
                'imagen': ''
            },
            {
                'nombre': 'Mouse Inalámbrico',
                'categoria': cat_tecnologia,
                'precio': 12990,
                'descripcion': 'Mouse ergonómico con batería de larga duración.',
                'imagen': ''
            }
        ]

        # 3. Iterar y crear productos
        for p in productos_data:
            obj, created = Producto.objects.get_or_create(
                nombre=p['nombre'],
                defaults={
                    'categoria': p['categoria'],
                    'precio': p['precio'],
                    'descripcion': p['descripcion'],
                    'imagen': p['imagen']
                }
            )
            
            # Usamos self.stdout.write en lugar de print
            if created:
                self.stdout.write(f"  + Creado: {p['nombre']}")
            else:
                self.stdout.write(f"  . Ya existe: {p['nombre']}")

        self.stdout.write(self.style.SUCCESS('¡Carga de datos finalizada correctamente!'))