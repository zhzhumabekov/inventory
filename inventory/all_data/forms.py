from django import forms
from .models import Person, Computer

class PersonForm(forms.ModelForm):
    """Форма модели персонала"""

    class Meta:
        model = Person
        fields = ('name', 'computer')


class ComputerForm(forms.ModelForm):
    """Форма модели компьютера"""

    class Meta:
        model = Computer
        fields = ('inventary_number', 'serial_number', 'computer_name')