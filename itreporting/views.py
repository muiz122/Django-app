from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Module
from .forms import RegistrationForm
import requests

def home(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={},{}&units=metric&appid={}'
    cities = [('Sheffield', 'UK'), ('Melaka', 'Malaysia'), ('Bandung', 'Indonesia')]
    weather_data = []
    api_key = '183f9de509264efdae89f36f19fb28bc'

    for city in cities:
        city_weather = requests.get(url.format(city[0], city[1], api_key)).json()
        weather = {
            'city': city_weather['name'] + ', ' + city_weather['sys']['country'],
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description']
        }
        weather_data.append(weather)

    return render(request, 'itreporting/home.html', {'title': 'Homepage', 'weather_data': weather_data})

def about(request):
    return render(request, 'itreporting/about.html')

def contact(request):
    return render(request, 'itreporting/contact.html')

def register_for_course(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST, user=request.user)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.student = request.user
            registration.save()
            messages.success(request, "You have successfully registered for the course!")
            return redirect('itreporting:module-list')
    else:
        form = RegistrationForm(user=request.user)

    return render(request, 'itreporting/registration_form.html', {'form': form})

class ModuleListView(ListView):
    model = Module
    ordering = ['-date_added']
    template_name = 'itreporting/module_list.html'
    context_object_name = 'modules'
    paginate_by = 10

class ModuleDetailView(DetailView):
    model = Module
    template_name = 'itreporting/module_detail.html'

class ModuleCreateView(LoginRequiredMixin, CreateView):
    model = Module
    fields = ['name', 'description', 'instructor']

    def form_valid(self, form):
        form.instance.instructor = self.request.user
        return super().form_valid(form)

class ModuleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Module
    success_url = reverse_lazy('module-list')

    def test_func(self):
        module = self.get_object()
        return self.request.user == module.instructor

