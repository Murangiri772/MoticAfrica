from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')





def battle(request):
    return render(request, 'battle.html')


def gallery(request):
    return render(request, 'gallery.html')


