from django.contrib import messages
from django.shortcuts import redirect, render
from apps.contacts.models import Contact
from apps.general.models import General
from apps.categories.models import MainCategory


def contacts(request):
    if request.method != "POST":
        return render(request, 'contact.html')
    user = request.user
    name, email, title, message = (request.POST.get("name"),
                                   request.POST.get("email"),
                                   request.POST.get("title"),
                                   request.POST.get("message"))
    if request.user.is_authenticated:
       name, email = user.first_name, user.email
    elif not (name and email):
        messages.error(request, 'Ism va emailn kiriting')
    
    Contact.objects.create(name=name, email=email,user=user, title=title, message=message)
    messages.success(request, 'Habaringiz yuborildi')
    # message.add_message(request, level=40, message='yuborshimiz kere bo'gan message')  ### buni yordamida messageni levelini o'zimiz bervorolimiza 
    return redirect('contacts-page')