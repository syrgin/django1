from django.http import HttpResponse, HttpResponseNotFound, Http404


def index(request):
    return HttpResponse('Страница приложения women.')

def categories(request, catid):
    if(request.POST):
        print(request.POST)
    return HttpResponse(f'<h1>Статьи по категориям <h1><p>{catid}</p>')

def archive(request, year):
    if int(year) > 2021:
        raise Http404()
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')