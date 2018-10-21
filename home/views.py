from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from home.forms import ContactForm
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.contrib import messages
from contextlib import contextmanager

# Create your views here.
def index(request):
    """A view that displays the index page"""
    return render(request, "index.html")
    
def about(request):
    """A view that displays the about page"""
    return render(request, "about.html")

"""
def contact(request):
  if request.method == 'POST':
    return redirect(reverse('index'))
  else:
      return render(request, "contact.html")
"""   
      
def email(request):

    subject = ''
    message = ''
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['heldervieiraster@gmail.com',]

    send_mail( subject, message, email_from, recipient_list )

    return redirect('redirect to a new page')
    
    
def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.html')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Kambolife" +'',
                ['kambolife@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            messages.success(request, 'Your message has been successfully sent. Many thanks!')
            return redirect('index')

    return render(request, 'contact.html', {
        'form': form_class,
    })