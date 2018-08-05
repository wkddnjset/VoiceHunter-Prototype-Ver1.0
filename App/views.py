from django.shortcuts import render
from django.utils import translation

# Create your views here.
def HomePage(request, lang):
    translation.activate(lang)
    return render(request, 'Home/HomePage.html', {
        'lang':lang
    })

def ProjectListPage(request, lang):
    translation.activate(lang)
    return render(request, 'Project/ProjectListPage.html', {})