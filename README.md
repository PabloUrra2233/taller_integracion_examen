# Catálogo de Librería – Taller de Integración

Aplicación web desarrollada con **Django** y **SQLite** que permite buscar productos de una librería por nombre y categoría.  
Está pensada como proyecto para la presentación final del ramo, cumpliendo los requisitos de:

- Uso de **Django** y su **ORM** (sin queries SQL manuales).
- Modelo de datos con relaciones (Producto–Categoría).
- Formularios de Django para búsqueda.
- Base de datos **SQLite**.
- Interfaz web con **Bootstrap** y hoja de estilos propia.

---

## Funcionalidad

- **Listado de productos** de librería (por ejemplo: cuadernos, lápices, libros, etc.).
- **Buscador por nombre** de producto.
- **Filtro por categoría** mediante un selector en el nav-bar.
- Visualización de:
  - nombre del producto,
  - categoría,
  - imagen (URL),
  - precio formateado,
  - descripción (truncada en la card, completa en BD).
- Panel de administración de Django para:
  - crear / editar / eliminar **categorías**,
  - crear / editar / eliminar **productos**.

---

## Tecnologías utilizadas

- **Python 3**
- **Django 5**
- **SQLite** (base de datos por defecto de Django)
- **Bootstrap 5** (estilos base)
- **CSS propio** (`catalogo/static/catalogo/styles.css`)

---

## Estructura principal del proyecto

```text
taller_integracion_examen/
├─ manage.py
├─ libreria/                # Proyecto Django
│  ├─ settings.py
│  ├─ urls.py
│  └─ ...
└─ catalogo/                # Aplicación principal
   ├─ models.py             # Modelos Categoria y Producto
   ├─ views.py              # Vista lista_productos
   ├─ urls.py               # URLs de la app
   ├─ forms.py              # Formulario de búsqueda
   ├─ admin.py              # Registro de modelos en el admin
   ├─ templates/
   │  └─ catalogo/
   │     └─ lista_productos.html
   └─ static/
      └─ catalogo/
         └─ styles.css

