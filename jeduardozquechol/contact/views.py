from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm
# Create your views here.


def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            subject = request.POST.get('subject', '')
            content = request.POST.get('content', '')
            # Enviamos el correo
            email = EmailMessage(
                "Asunto: {}".format(subject),
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                "no-contestar@jeduardozquechol.com",
                #Correo a donde llegara
                ["contacteduzq@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('contact')+"?ok")
            except:
                # Algo no salió bien
                return redirect(reverse('contact')+"?fail")

    return render(request, 'contact/contact.html', {'form': contact_form})
