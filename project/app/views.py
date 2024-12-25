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
        contact = Contact(name=name, email=email, message=message)
        contact.save()
        # contactdata = {
        #     "name": name,
        #     "email": email,
        #     "message": message,
        # }
        contactdata = f"\tName: {name} \n \t Email: {email} \n \tMessage: {message}"

        
        return render(request, 'contact.html', {'contactdata': contactdata})
    return render(request, "contact.html")