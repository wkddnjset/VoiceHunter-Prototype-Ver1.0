from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from .models import *
import json

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

    context = {
        'pk':project.id,
        'message': message}
    return HttpResponse(json.dumps(context), content_type="application/json")

@require_http_methods(["POST"])
def CreateUserAPI(request):
    pass