from django.db.models import query
from .models import Superhero
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request):
    all_heroes = Superhero.objects.all()
    context = {
        'all_heroes': all_heroes
    }
    return render(request, 'superheroes/index.html', context)

def detail(request, hero_id):
    single_hero = Superhero.objects.get(pk=hero_id)
    context = {
        'single_hero': single_hero
    }
    return render(request, 'superheroes/detail.html/', context)

def create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        alter_ego = request.POST.get("alter_ego")
        primary = request.POST.get("primary")
        secondary = request.POST.get("secondary")
        catchphrase = request.POST.get("catchphrase")
        new_hero = Superhero(name=name, alter_ego=alter_ego, primary_ability=primary, secondary_ability=secondary, catch_phrase=catchphrase)
        new_hero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request, 'superheroes/create.html')

def delete_hero(request, hero_id):
    hero = Superhero.objects.get(pk=hero_id)
    hero.delete()
    return render(request, 'superheroes/delete.html/')


def edit(request):
    if request.method == "POST":
        name = request.POST.get("name")
        alter_ego = request.POST.get("alter_ego")
        primary = request.POST.get("primary")
        secondary = request.POST.get("secondary")
        catchphrase = request.POST.get("catchphrase")
        edit_hero = Superhero(name=name, alter_ego=alter_ego, primary_ability=primary, secondary_ability=secondary, catch_phrase=catchphrase)
        edit_hero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request, 'superheroes/edit.html')