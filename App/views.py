from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect
from django.utils import translation
from django.shortcuts import render
from .forms import ProjectForm
from .models import *
import json
# Create your views here.
def HomePage(request, lang='ko'):
    translation.activate(lang)
    projects = Project.objects.all()

    item_list = []
    for project in projects[:6]:
        dict = {}
        dict['project'] = project
        dict['apply'] = len(ProjectApply.objects.filter(project=project))
        dict['tags'] = ProjectTag.objects.filter(project=project)[:3]
        item_list.append(dict)
    return render(request, 'Home/HomePage.html', {
        'lang':lang,
        'items':item_list,
    })

def ProjectListPage(request, lang='ko'):
    translation.activate(lang)
    search = request.GET.get('q')
    page = request.GET.get('page')
    if search == None:
        search = ""
    if page == None:
        page = 1

    projects = Project.objects.all()
    item_list = []
    for project in projects:
        dict = {}
        dict['project'] = project
        dict['apply'] = len(ProjectApply.objects.filter(project=project))
        dict['tags'] = ProjectTag.objects.filter(project=project)[:6]
        item_list.append(dict)

    paginator = Paginator(item_list, 1)
    contacts = paginator.get_page(page)

    return render(request, 'ProjectList/ProjectListPage.html', {
        'lang': lang,
        'search': search,
        'page': page,
        'items': contacts,
        'projects_len':len(projects),
    })

def ProjectCreatePage(request, lang='ko'):
    translation.activate(lang)

    if request.method == "POST":
        form = ProjectForm(request.POST)
        print(form)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
        return redirect('App:detail-projects', pk=post.id, lang='ko')
    else:
        form = ProjectForm()

    tags = Tag.objects.all()
    return render(request, 'ProjectCreate/ProjectCreatePage.html', {
        'lang': lang,
        'form': form,
        'tags': tags
    })

def ProjectDetailPage(request, pk, lang='ko'):
    translation.activate(lang)

    project = Project.objects.get(pk=pk)
    item = {}
    item['project'] = project
    item['apply'] = len(ProjectApply.objects.filter(project=project))
    item['tags'] = ProjectTag.objects.filter(project=project)[:6]

    return render(request, 'ProjectDetail/ProjectDetailPage.html', {
        'lang': lang,
        'item':item,
    })

@login_required
@require_http_methods(["POST"])
def CreateProjectAPI(request):
    title = request.POST.get('title', None)
    gugun = request.POST.get('gugun', None)
    type = request.POST.get('type', None)
    gender = request.POST.get('gender', None)
    cost = request.POST.get('cost', None)
    period = request.POST.get('period', None)
    deadline = request.POST.get('deadline', None)
    content = request.POST.get('content', None)
    start_at = request.POST.get('start_at', None)
    tags = request.POST.get('tags', None)

    try:
        project = Project.objects.create(
            user=request.user,
            title=title,
            gugun=Gugun.objects.get(pk=gugun),
            type=type,
            gender=gender,
            cost=int(cost),
            period=int(period),
            deadline=deadline,
            content=content,
            start_at=start_at
        )
        print('프로젝트 생성')
        try:
            for tag_id in tags.split(','):
                ProjectTag.objects.create(
                    project=project,
                    tag=Tag.objects.get(pk=tag_id)
                )
            message = 'success'
            print('태그관계 생성')
        except:
            project.delete()
            message = 'error'
            print('프로젝트 삭제 생성')
    except:
        message = 'error'
    # print(title)
    # print(gugun)
    # print(type)
    # print(gender)
    # print(cost)
    # print(period)
    # print(deadline)
    # print(content)
    # print(start_at)
    # print(tags)

    context = {
        'pk':project.id,
        'message': message}
    return HttpResponse(json.dumps(context), content_type="application/json")

