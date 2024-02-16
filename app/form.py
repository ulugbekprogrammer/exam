from django.forms import ModelForm
from .models import *

class BookForm(ModelForm):
    class Meta:
        model = Math
        fields = '__all__'