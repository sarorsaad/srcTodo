from django.forms import ModelForm
from .models import *

class NewTodoForm(ModelForm):
    class Meta:
        model = Todo
        fields =['text']
