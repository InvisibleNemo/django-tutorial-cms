
from urllib import request
from django.core.mail import send_mail
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.template import context
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm
from django.views import generic
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from agents.mixins import OrganizerAndLoginRequiredMixin


class SignUpView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm
    
    def get_success_url(self):
        return reverse("login")


class LandingPageView(LoginRequiredMixin, TemplateView):
    template_name = "landing.html"

class LeadListView(LoginRequiredMixin, ListView):
    template_name: str = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"

    def get_queryset(self):
        user = self.request.user
        if user.is_organizer:
            queryset = Lead.objects.filter(organization=user.userprofile) # initial queryset
        elif user.is_agent:
            queryset = Lead.objects.filter(organization=user.agent.organization)
            queryset = queryset.filter(agent__user=user) # filter for the agent logged in        
        return queryset
        # return super().get_queryset()
    

class LeadDetailView(LoginRequiredMixin, DetailView):
    template_name: str = "leads/lead_detail.html"
    def get_queryset(self):
        user = self.request.user
        if user.is_organizer:
            queryset = Lead.objects.filter(organization=user.userprofile) # initial queryset
        elif user.is_agent:
            queryset = Lead.objects.filter(organization=user.agent.organization)
            queryset = queryset.filter(agent__user=user) # filter for the agent logged in        
        return queryset
    context_object_name = "lead"

class LeadCreateView(OrganizerAndLoginRequiredMixin, CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")
    
    def form_valid(self, form: LeadForm) -> HttpResponse:
        # TODO send email
        send_mail(
            subject="Lead created",
            message="Go to the site to view.",
            from_email="test@test.com",
            recipient_list=["test2@test.com"]
        )
        return super(LeadCreateView, self).form_valid(form)

class LeadUpdateView(OrganizerAndLoginRequiredMixin, UpdateView):
    template_name = "leads/lead_update.html"
    form_class = LeadModelForm
    def get_queryset(self):
        user = self.request.user
        if user.is_organizer:
            queryset = Lead.objects.filter(organization=user.userprofile) # initial queryset
        
        return queryset
    

    def get_success_url(self):
        return reverse("leads:lead-list")

class LeadDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "leads/lead_delete.html"
    def get_queryset(self):
        user = self.request.user
        if user.is_organizer:
            queryset = Lead.objects.filter(organization=user.userprofile) # initial queryset        
        return queryset

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