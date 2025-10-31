from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>✅ Welcome Rahul! Django Server is Running Successfully!</h1>")
