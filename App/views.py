from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.utils import translation
from .models import *
# Create your views here.
def HomePage(request, lang='ko'):
    translation.activate(lang)
    projects = Project.objects.all()

    item_list = []
    for project in projects[:6]:
        dict = {}
        dict['project'] = project
        dict['apply'] = len(ProjectApply.objects.filter(project=project))
        dict['tags'] = ProjectTag.objects.filter(project=project)
        item_list.append(dict)
    return render(request, 'Home/HomePage.html', {
        'lang':lang,
        'items':item_list,
    })

def ProjectListPage(request, lang='ko'):
    translation.activate(lang)
    search = request.GET.get('q')
    if search == None:
        search = ""

    projects = Project.objects.all()

    item_list = []
    for project in projects:
        dict = {}
        dict['project'] = project
        dict['apply'] = len(ProjectApply.objects.filter(project=project))
        dict['tags'] = ProjectTag.objects.filter(project=project)[:6]
        item_list.append(dict)

    paginator = Paginator(item_list, 1)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)

    return render(request, 'ProjectList/ProjectListPage.html', {
        'lang': lang,
        'search' : search,
        'items':contacts,
    })

def ProjectCreatePage(request, lang='ko'):
    translation.activate(lang)
    return render(request, 'ProjectCreate/ProjectCreatePage.html', {
        'lang': lang
    })