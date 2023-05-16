from django.shortcuts import render
from .models import Clients, Seasons, Tours, Trips
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_clients=Clients.objects.all().count()
    num_seasons=Seasons.objects.all().count()
    num_seasons_available=Seasons.objects.filter(closed=0).count()
    num_tours=Tours.objects.count()
    num_trips=Trips.objects.count()# Метод 'all()' применён по умолчанию.

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_clients':num_clients,'num_seasons':num_seasons,'num_seasons_available':num_seasons_available,'num_tours':num_tours, 'num_trips':num_trips},
    )

class ClientsListView(generic.ListView):
    model = Clients
    context_object_name = 'my_clients_list'
    template_name = 'clients.html'

class ClientsDetailView(generic.DetailView):
    model = Clients
    template_name = 'clients_detail.html'

class ClientsCreate(CreateView):
    model = Clients
    fields = '__all__'
    template_name = 'clients_form.html'

class ClientsUpdate(UpdateView):
    model = Clients
    fields = ['name','last_name','middle_name','passport']
    template_name = 'clients_form.html'

class ClientsDelete(DeleteView):
    model = Clients
    success_url = reverse_lazy('clients')
    template_name = 'clients_delete.html'

#

class ToursListView(generic.ListView):
    model = Tours
    context_object_name = 'my_tours_list'
    template_name = 'tours.html'

class ToursDetailView(generic.DetailView):
    model = Tours
    template_name = 'tours_detail.html'

class ToursCreate(CreateView):
    model = Tours
    fields = '__all__'
    template_name = 'clients_form.html'

class ToursUpdate(UpdateView):
    model = Tours
    fields = ['season_id','price','city','name', 'info']
    template_name = 'clients_form.html'

class ToursDelete(DeleteView):
    model = Tours
    success_url = reverse_lazy('tours')
    template_name = 'clients_delete.html'

#

class TripsListView(generic.ListView):
    model = Trips
    context_object_name = 'my_trips_list'
    template_name = 'trips.html'

class TripsDetailView(generic.DetailView):
    model = Trips
    template_name = 'trips_detail.html'

class TripsCreate(CreateView):
    model = Trips
    fields = '__all__'
    template_name = 'clients_form.html'

class TripsUpdate(UpdateView):
    model = Trips
    fields = ['tour_id', 'client_id']
    template_name = 'clients_form.html'

class TripsDelete(DeleteView):
    model = Trips
    success_url = reverse_lazy('trips')
    template_name = 'clients_delete.html'

#

class SeasonsListView(generic.ListView):
    model = Seasons
    context_object_name = 'my_seasons_list'
    template_name = 'seasons.html'

class SeasonsDetailView(generic.DetailView):
    model = Seasons
    template_name = 'seasons_detail.html'

class SeasonsCreate(CreateView):
    model = Seasons
    fields = '__all__'
    template_name = 'clients_form.html'

class SeasonsUpdate(UpdateView):
    model = Seasons
    fields = ['name','last_name','middle_name','passport']
    template_name = 'clients_form.html'

class SeasonsDelete(DeleteView):
    model = Seasons
    success_url = reverse_lazy('seasons')
    template_name = 'clients_delete.html'
