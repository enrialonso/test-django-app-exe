from django.shortcuts import render
import random

from .models import Modelo
import string


def random_string(stringLength=10):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(stringLength))


def index(request):
    save = Modelo(campo=random_string())
    save.save()
    res = Modelo.objects.filter().all()
    data, data['data'] = {}, [i.__dict__ for i in res]
    return render(request, 'core/index.html', data)
