from django.shortcuts import render, redirect
from .models import Contact

# Create your views here.
def index(request):
    return render(request, "index.html")
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        location = request.POST.get("location")
        priority = request.POST.get("priority")
        
        contact = Contact(
            name=name, 
            email=email, 
            message=message,
            location=location,
            priority=priority
        )
        contact.save()
        return redirect('contact')
    return render(request, "contact.html")