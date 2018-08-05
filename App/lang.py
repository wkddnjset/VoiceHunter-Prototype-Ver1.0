from django.views.decorators.http import require_http_methods
from django.utils import translation
from django.http import JsonResponse

def transLangEN(request):
    userLanguage = 'en'
    translation.activate(userLanguage)
    request.session[translation.LANGUAGE_SESSION_KEY] = userLanguage

    return JsonResponse({'return':'success'})

@require_http_methods(["POST"])
def transLangKO(request):
    print("한글로 바꾸기")
    userLanguage = 'ko'
    translation.activate(userLanguage)
    request.session[translation.LANGUAGE_SESSION_KEY] = userLanguage

    return JsonResponse({'return':'success'})