# views.py
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect

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

def services(request):
    return render(request, 'templates/services.html')

def softwaredevelopment(request):
    """
    Handles the software development request form:
    - sends an email to ADMIN_EMAIL (or DEFAULT_FROM_EMAIL)
    - sends a confirmation email to the user
    - uses messages framework for success/error feedback
    """
    if request.method == "POST":
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        company = request.POST.get('company', 'Not provided').strip()
        service = request.POST.get('service', '').strip() or 'Not specified'
        message_text = request.POST.get('message', '').strip()

        # Basic validation
        if not name or not email or not message_text:
            messages.error(request, "Please fill in all required fields (Name, Email, Message).")
            return HttpResponseRedirect(request.path_info)  # redirect back to page

        subject = f"New Software Dev Request from {name}"
        body = (
            f"New software development request:\n\n"
            f"Name: {name}\n"
            f"Email: {email}\n"
            f"Company: {company}\n"
            f"Service: {service}\n\n"
            f"Message:\n{message_text}\n"
        )

        from_email = getattr(settings, 'DEFAULT_FROM_EMAIL', None) or getattr(settings, 'EMAIL_HOST_USER', None)
        admin_email = getattr(settings, 'ADMIN_EMAIL', from_email)

        try:
            # send to admin
            send_mail(subject, body, from_email, [admin_email], fail_silently=False)

            # confirmation to user
            user_subject = "Thanks — we received your project request"
            user_message = (
                f"Hi {name},\n\n"
                "Thanks for contacting us about your project. Here is a copy of your request:\n\n"
                f"Service: {service}\n"
                f"Message: {message_text}\n\n"
                "One of our team members will contact you within 24 hours.\n\n"
                "Best,\nYour Company Team"
            )
            send_mail(user_subject, user_message, from_email, [email], fail_silently=False)

            messages.success(request, "Thank you — your request has been sent. We'll contact you shortly.")
            return HttpResponseRedirect(request.path_info)
        except BadHeaderError:
            messages.error(request, "Invalid header found.")
            return HttpResponseRedirect(request.path_info)
        except Exception as e:
            messages.error(request, f"There was an error sending your request: {e}")
            return HttpResponseRedirect(request.path_info)

    return render(request, 'templates/softwaredevelopment.html')

def contact(request):
    thank_you_message = ""
    if request.method == "POST":
        full_name = request.POST.get('full_name', '').strip()
        email = request.POST.get('email', '').strip()
        message_text = request.POST.get('message', '').strip()

        subject = f"New message from {full_name or 'Unknown'}"
        message_body = (
            f"Name: {full_name}\n"
            f"Email: {email}\n\n"
            f"Message:\n{message_text}"
        )

        from_email = getattr(settings, 'EMAIL_HOST_USER', None)
        recipient = getattr(settings, 'ADMIN_EMAIL', from_email)

        try:
            send_mail(subject, message_body, from_email, [recipient], fail_silently=False)
            thank_you_message = "Thank you for reaching out! We will get back to you soon."
            messages.success(request, thank_you_message)
            return HttpResponseRedirect(request.path_info)
        except BadHeaderError:
            messages.error(request, "Invalid header found.")
            return HttpResponseRedirect(request.path_info)
        except Exception as e:
            messages.error(request, f"There was an error sending your message: {e}")
            return HttpResponseRedirect(request.path_info)

    return render(request, 'templates/contact.html', {'thank_you_message': thank_you_message})


def callcenter(request):
    """
    Accepts POST from the call center form, sends notification to admin
    and a confirmation email to the user (if provided). Uses messages
    framework to show success/error in the template.
    """
    if request.method == 'POST':
        full_name = request.POST.get('full_name', '').strip()
        email = request.POST.get('email', '').strip()
        company = request.POST.get('company', 'Not provided').strip()
        message = request.POST.get('message', '').strip()

        # Basic validation
        if not full_name or not email or not message:
            messages.error(request, "Please fill in all required fields.")
            return HttpResponseRedirect(request.path_info + '#contact')

        subject = f'New Call Center Consultation Request from {full_name}'
        email_body = (
            f"New consultation request from your Call Center page:\n\n"
            f"Name: {full_name}\n"
            f"Email: {email}\n"
            f"Company: {company}\n\n"
            f"Message:\n{message}\n"
        )

        from_email = getattr(settings, 'DEFAULT_FROM_EMAIL', None) or getattr(settings, 'EMAIL_HOST_USER', None)
        admin_email = getattr(settings, 'ADMIN_EMAIL', from_email)

        try:
            # Email to admin
            send_mail(subject, email_body, from_email, [admin_email], fail_silently=False)

            # Confirmation email to user (optional but helpful)
            user_subject = "Thank you for your interest in our Call Center Services"
            user_message = (
                f"Dear {full_name},\n\n"
                "Thank you for contacting us about our call center solutions. "
                "We have received your request and one of our specialists will "
                "contact you within 24 hours to discuss your needs.\n\n"
                "Best regards,\nYour Company Team"
            )

            send_mail(user_subject, user_message, from_email, [email], fail_silently=False)

            messages.success(request, 'Thank you for your interest! We will contact you shortly.')
            # Redirect back to the contact section so the user sees the message
            return HttpResponseRedirect(request.path_info + '#contact')

        except BadHeaderError:
            messages.error(request, 'Invalid header found.')
            return HttpResponseRedirect(request.path_info + '#contact')
        except Exception as e:
            messages.error(request, f'There was an error sending your message: {str(e)}')
            return HttpResponseRedirect(request.path_info + '#contact')

    # GET -> render template
    return render(request, 'templates/callcenter.html')

def digitalmarketing(request):
    return render(request, 'templates/digitalmarketing.html')


def medicalbilling(request):
    return render(request, 'templates/medicalbilling.html')

def contentwriting(request):
    return render(request, 'templates/contentwriting.html')

def itconsultancy(request):
    return render(request, 'templates/itconsultancy.html')

def muhammadjamalraja(request):
    return render(request, 'templates/muhammadjamalraja.html')

