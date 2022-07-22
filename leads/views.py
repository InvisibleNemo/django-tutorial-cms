
from urllib import request
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.template import context
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm

from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView



class LandingPageView(TemplateView):
    template_name = "landing.html"

class LeadListView(ListView):
    template_name: str = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"

class LeadDetailView(DetailView):
    template_name: str = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"

class LeadCreateView(CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")

class LeadUpdateView(UpdateView):
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")

class LeadDeleteView(DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead-list")


# Create your views here.

# def landing_page(request):
#     return render(request, 'landing.html')

# def lead_list(request):
#     # return HttpResponse("Hello world")

#     leads = Lead.objects.all()

#     # context = {
#     #     "leads": leads,
#     #     "age": 35
#     # }

#     context ={
#         "leads": leads
#     }

#     return render(request, "leads/lead_list.html", context)


# def lead_detail(request, pk):
#     # print(pk)

#     lead = Lead.objects.get(id=pk)

#     context = {
#         "lead": lead
#     }

#     return render(request, "leads/lead_detail.html", context)

#     # return HttpResponse("Here is the detail view")

# def lead_create(request):
#     # print(request.POST)

#     if request.method == "POST":
#         print('Receiving a POST')
#         form = LeadModelForm(request.POST)

#         if form.is_valid():
#             # print(form.cleaned_data)
#             form.save()
#             # print('Lead created')
#             return redirect("/leads")
#     else:
#         form = LeadModelForm()
#     context = {
#         "form": form
#     }
#     return render(request, "leads/lead_create.html", context)

# def lead_update(request, pk):

#     lead = Lead.objects.get(id=pk)
#     form = LeadModelForm(instance=lead)
#     if request.method == "POST":
#         print('Receiving a POST')
#         form = LeadModelForm(request.POST, instance=lead)
#         if form.is_valid():
#             form.save()
#             return redirect("/leads")
#     context = {
#         "form": form,
#         "lead": lead
#     }
#     return render(request, "leads/lead_update.html", context)

# def lead_delete(request, pk):

#     lead = Lead.objects.get(id=pk)
#     lead.delete()
#     return redirect("/leads")

# def lead_update(request, pk):

#     lead = Lead.objects.get(id=pk)
#     form = LeadForm()
#     if request.method == "POST":
#             print('Receiving a POST')
#             form = LeadForm(request.POST)

#             if form.is_valid():
#                 # print(form.cleaned_data)

#                 first_name = form.cleaned_data['first_name']
#                 last_name = form.cleaned_data['last_name']
#                 age = form.cleaned_data['age']
                
#                 lead.first_name = first_name
#                 lead.last_name = last_name
#                 lead.age = age
#                 lead.save()
                
#                 # print('Lead upated')
#                 return redirect("/leads")
#     context = {
#         "form": form,
#         "lead": lead
#     }

#     return render(request, "leads/lead_update.html", context)

# def lead_create(request):
#     print(request.POST)

#     if request.method == "POST":
#         print('Receiving a POST')
#         form = LeadModelForm(request.POST)

#         if form.is_valid():
#             # print(form.cleaned_data)

#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             agent = Agent.objects.first()
#             Lead.objects.create(
#                 first_name = first_name,
#                 last_name = last_name,
#                 age = age,
#                 agent = agent
#             )
#             # print('Lead created')
#             return redirect("/leads")
#     else:
#         form = LeadModelForm()
#     context = {
#         "form": form
#     }
#     return render(request, "leads/lead_create.html", context)