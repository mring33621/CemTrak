from django.http import HttpResponse


def index(request):
    return HttpResponse("CemTrak Project index page... <a href='/admin'>Admin</a>")