from django import forms
from .models import Articulo

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['titulo',  'contenido', 'categoria', 'imagen']
        widgets = {
            'contenido': forms.Textarea(attrs={
                'class': 'textarea_custom1',
                'rows': 10,
                'cols': 80,  
            }),
        }


#Esto edite
#         