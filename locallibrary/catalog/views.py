# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def index(request):
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html')