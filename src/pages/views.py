from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    print(request.user)
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, 'home.html', {})

def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html')


def about_view(request, *args, **kwargs):
    context = {
        'text': 'This is about us',
        'phone': '+38098765434',
        'authors': ['Alex', 'Daisy', 'Grand'],
    }
    return render(request, 'about.html', context)