from django.http import HttpResponse

def index(request):
    return HttpResponse("✅ Todo App is working correctly!")

