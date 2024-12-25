from django.shortcuts import render, redirect
from .models import Contact

# Create your views here.
def index(request):
    return render(request, "index.html")
def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]
        contact = Contact(name=name, email=email, message=message)
        contact.save()
        return redirect("contact")
    return render(request, "contact.html")