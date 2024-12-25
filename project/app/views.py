from django.shortcuts import render

# Create your views here.
def index(request):
    print("Hello to the index page")
    welcome = "Welcome to the index page"
    return render(request, "index.html",{ "greetings": welcome})