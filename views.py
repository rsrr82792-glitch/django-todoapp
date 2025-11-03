from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to Django Todo App Home!and this is so exciting</h1>")

