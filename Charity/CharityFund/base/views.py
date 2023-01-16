from django.shortcuts import render, redirect
from base.form import charities
from base.models import charity

def main(request):
    return redirect('/home/')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about-us.html')

def all(request):
    data = charity.objects.all()
    return render(request, 'charity.html', {'data': data})

def add(request):
    if request.method == 'POST':
        form = charities(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/all/')
    else:
        return render(request, 'add-charity.html')


def delete(request, id):
    chrty = charity.objects.get(id=id)
    chrty.delete()
    return redirect('/all/')


def edit(request, id):
    chrty = charity.objects.get(id=id)
    return render(request, 'edit.html', {'charity': chrty})


def update(request, id):
    chirty = charity.objects.get(id=id)
    charty = charities(request.POST, instance=chirty)
    if charty.is_valid:
        charty.save()
        return redirect('/all/')
    else:
        return render(request, 'edit.html', {'charity': chirty})


