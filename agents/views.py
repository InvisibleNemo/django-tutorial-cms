from django.shortcuts import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from .forms import AgentModelForm
from django.core.mail import send_mail
from .mixins import OrganizerAndLoginRequiredMixin

# Create your views here.


class AgentListView(OrganizerAndLoginRequiredMixin, generic.ListView):
    template_name: str = "agents/agent_list.html"
    
    def get_queryset(self):
        # return Agent.objects.all()
        request_user_organization = self.request.user.userprofile
        return Agent.objects.filter(organization=request_user_organization)
    
    
class AgentCreateView(OrganizerAndLoginRequiredMixin, generic.CreateView):
    template_name: str = "agents/agent_create.html"
    form_class = AgentModelForm
    
    def get_success_url(self):
        return reverse("agents:agent-list")
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_agent = True
        user.is_organizer = False
        user.save()
        Agent.objects.create(
            user=user,
            organization=self.request.user.userprofile,
        )
        # agent.organization = self.request.user.userprofile
        # agent.save()
        # TODO send email
        send_mail(
            subject="You are invited to be an agent",
            message="Go to the site to view.",            
            from_email="admin@test.com",
            recipient_list=[user.email]   
        )
        return super(AgentCreateView, self).form_valid(form)
    
class AgentDetailView(OrganizerAndLoginRequiredMixin, generic.DetailView):
    template_name: str = "agents/agent_detail.html"
    queryset = Agent.objects.all()
    context_object_name = "agent"

class AgentUpdateView(OrganizerAndLoginRequiredMixin, generic.UpdateView):
    template_name = "agents/agent_update.html"
    queryset = Agent.objects.all()
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse("agents:agent-list")

class AgentDeleteView(OrganizerAndLoginRequiredMixin, generic.DeleteView):
    template_name = "agents/agent_delete.html"
    context_object_name = "agent"
    
    queryset = Agent.objects.all()

    def get_success_url(self):
        return reverse("agents:agent-list")
