from django.shortcuts import render, HttpResponseRedirect
from .forms import ContactForm, AuthorForm
from django.contrib import messages

# Create your views here.

def contact(request):
    submitted = False

    form = ContactForm()
    if request.method == 'POST':
        contact_data = request.POST
        form = ContactForm(data=contact_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mesajınız qeydə alındı')
            print('Form save')
            return HttpResponseRedirect('/contact?submitted=True')
        else:
            print('Form is invalid')
    context = { 
        'form':form
    }
    return render(request, 'contact.html', context)


def author(request):
    submitted = False

    form = AuthorForm()
    if request.method == 'POST':
        author_data = request.POST
        form = AuthorForm(data=author_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mesajınız qeydə alındı')
            print('Form save')
            return HttpResponseRedirect('/author?submitted=True')
        else:
            print('Form is invalid')
    context = { 
        'form':form
    }
    return render(request, 'author.html', context)