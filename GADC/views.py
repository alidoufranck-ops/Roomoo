from django.shortcuts import render
from .forms import RegisterFormulaireForm
from .models import *
from django.shortcuts import redirect

# Create your views here.
def home(request):
    
    return render(request, 'base.html')

def formulaire(request):

    if request.method == 'POST':
        forms = RegisterFormulaireForm(request.POST)

        if forms.is_valid():
            forms.save()
            return redirect('/confirmation/')

    else:
        forms = RegisterFormulaireForm()


    return render(request, 'formulaire.html', {
        'forms': forms
    })


























def confirmation(request):
    return render(request, 'affiche.html', context = {'demande': Formulaire.objects.all() })