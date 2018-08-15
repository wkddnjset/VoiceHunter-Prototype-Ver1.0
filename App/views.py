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
    search = request.GET.get('q')
    return render(request, 'ProjectList/ProjectListPage.html', {
        'lang': lang,
        'search' : search
    })

def ProjectCreatePage(request, lang):
    translation.activate(lang)
    return render(request, 'ProjectCreate/ProjectCreatePage.html', {
        'lang': lang
    })