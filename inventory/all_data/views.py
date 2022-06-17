from django.shortcuts import render
from .models import Person, Computer
from .forms import PersonForm, ComputerForm

def index(request):
    peron_forms = PersonForm(request.POST or None)
    computer_forms = ComputerForm(request.POST or None)
    context = {
        'person_forms': peron_forms,
        'computer_forms': computer_forms
    }
    return render(request, 'base.html', context)
