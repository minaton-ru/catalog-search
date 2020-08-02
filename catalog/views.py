from django.shortcuts import render
from catalog.models import Car
from catalog.forms import SearchForm
from django.http import HttpResponse
from django.template import loader
from django.http.response import HttpResponseRedirect
from django.views.generic import TemplateView, ListView, FormView
from django.db.models import Q


class index(ListView):
    template_name = 'index.html'
    model = Car

def index_search(request):
    cars_count = Car.objects.all()
    if request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            #if form.cleaned_data['manufacturer'] is not None:
            #    manufacturer = form.cleaned_data['manufacturer'] 
            if form.cleaned_data['model'] is not None:
                model = form.cleaned_data['model']
                if form.cleaned_data['gearbox'] != 4:
                    gearbox = form.cleaned_data['gearbox']
                    object_list = Car.objects.filter((Q(manufacturer__icontains=model) | Q(model__icontains=model) | Q(year__icontains=model)| Q(color__icontains=model)) & Q(gearbox__icontains=gearbox) )
                    return render(request, 'index.html', {'object_list': object_list, 'form': form, 'cars_count': cars_count})
                else:
                    object_list = Car.objects.filter(
                    Q(manufacturer__icontains=model) | Q(model__icontains=model) | Q(year__icontains=model) | Q(color__icontains=model))
                    return render(request, 'index.html', {'object_list': object_list, 'form': form, 'cars_count': cars_count})
            else:
                if form.cleaned_data['gearbox'] != 4:
                    gearbox = form.cleaned_data['gearbox']
                    object_list = Car.objects.filter(Q(gearbox__icontains=gearbox))
                    return render(request, 'index.html', {'object_list': object_list, 'form': form, 'cars_count': cars_count})
                else:
                    object_list = Car.objects.all()
                    return render(request, 'index.html', {'object_list': object_list, 'form': form, 'cars_count': cars_count})
    else:
        form = SearchForm()
        object_list = Car.objects.all()
        return render(request, 'index.html', {'object_list': object_list, 'form': form, 'cars_count': cars_count})

