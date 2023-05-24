
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        print(f'Получена контакная информация: {name}, тел.: {phone}, e-mail: {email}')
    return render(request, "contacts.html")