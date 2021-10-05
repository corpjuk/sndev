"""
Render home page

"""

#from django.http import HttpResponse
from django.shortcuts import render

def home_view(request, id=None, *args, **kwargs):
    # context = { 
    #     None,
    # }
    return render(request, 'home-view.html', context=None)