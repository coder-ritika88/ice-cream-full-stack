
from django.shortcuts import render
from home.models import Contact


def index(request):
    context = {
        'variable': "this is sent"
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            desc=desc
        )

        return render(request, 'contact.html', {'success': True})

    return render(request, 'contact.html')

