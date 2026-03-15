from django.shortcuts import render
from .ai_email import generate_email
from .models import *

def dashboard(request):

    email_text = ""

    if request.method == "POST":

        email_type = request.POST.get("email_type")
        receiver = request.POST.get("receiver")
        purpose = request.POST.get("purpose")
        sender = request.POST.get("sender")

        email_text = generate_email(email_type, receiver, purpose, sender)
        

    return render(request, "dashboard.html", {"email_text": email_text})