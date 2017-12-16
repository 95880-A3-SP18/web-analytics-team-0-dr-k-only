
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from django.db import IntegrityError

from .models import TodoItem


class IndexView(ListView):
    model = TodoItem
