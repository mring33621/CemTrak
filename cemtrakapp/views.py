from django.http import HttpResponse


def index(request):
    return HttpResponse("CemTrak App index page... <a href='/admin'>Admin</a>")