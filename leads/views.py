from django.shortcuts import render
from django.http import HttpResponse
from django.template import context
from .models import Lead
# Create your views here.

def home_page(request):
    # return HttpResponse("Hello world")

    leads = Lead.objects.all()

    context = {
        "leads": leads,
        "age": 35
    }

    return render(request, "second_page.html", context)


def lead_list(request):
