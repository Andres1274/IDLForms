from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from aplications.home.models import User


def dropdown(request):
    data = {
        'Users': User.objects.all()
    }
    return render(request, 'index.html', data)


class HomeListView(ListView):
    model = User
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Usuarios'
        return context
