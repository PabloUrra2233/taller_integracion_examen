from django import forms
from .models import Categoria, Producto



class BusquedaProductoForm(forms.Form):
    q = forms.CharField(
        label='',
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Buscar producto...',
                'class': 'form-control me-2',
            }
        ),
    )

    categoria = forms.ModelChoiceField(
        label='',
        required=False,
        queryset=Categoria.objects.none(),  # se rellena en __init__
        empty_label='Todas las categorías',
        widget=forms.Select(
            attrs={
                'class': 'form-select me-2',
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Cargamos las categorías reales cuando el form se crea
        self.fields['categoria'].queryset = Categoria.objects.all()

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['categoria', 'precio', 'stock', 'descripcion', 'imagen']
        widgets = {
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'imagen': forms.URLInput(attrs={'class': 'form-control'}),
        }
