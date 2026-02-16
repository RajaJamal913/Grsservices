from django.shortcuts import redirect, render

def index(request):
    return render(request, 'templates/index.html')

def about(request):
    return render(request, 'templates/about.html')
def Team(request):
    return render(request, 'templates/team.html')

def blog(request):
    return render(request, 'templates/blog.html')

def blog_single(request):
    return render(request, 'templates/blog-single.html')

# views.py

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings

from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def contact(request):
    thank_you_message = ""  # Initialize an empty message

    if request.method == "POST":
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        subject = f"New message from {full_name}"
        message_body = (
            f"Name: {full_name}\n"
            f"Email: {email}\n\n"
            f"Message:\n{message}"
        )

        # Send email using configured settings
        send_mail(
            subject,
            message_body,
            settings.EMAIL_HOST_USER,   # sender's email
            [settings.EMAIL_HOST_USER], # recipient's email (admin)
            fail_silently=False,
        )

        # Set the thank-you prompt message
        thank_you_message = "Thank you for reaching out! We will get back to you soon."

    return render(request, 'templates/contact.html', {'thank_you_message': thank_you_message})

def services(request):
    return render(request, 'templates/services.html')
