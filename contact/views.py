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
        # submitted = True
        if form.is_valid():
            form.save()
            messages.success(request, 'Mesajınız qeydə alındı')
            print('Form save')
            # submitted = True
            return HttpResponseRedirect('/contact?submitted=True')
        else:
            # form = ContactForm()
            # submitted = True
            print('Form is invalid')
    context = { 
        'form':form
    }
    # print(form)
    return render(request, 'contact.html', context)


def author(request):

    
    form = AuthorForm()
    if request.method == 'POST':
        author_data = request.POST
        form = AuthorForm(data=author_data)

        if form.is_valid():
            form.save()
            messages.success(request, 'Mesajınız qeydə alındı')
            print('Form save')
        else:
            print('Form is invalid')
    context = { 
        'form':form
    }

    return render(request, 'author.html', context)