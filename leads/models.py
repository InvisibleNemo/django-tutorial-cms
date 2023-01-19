from unicodedata import category
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import AbstractUser
# Create your models here.

# User = get_user_model()

class User(AbstractUser):
    is_organizer = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Lead(models.Model):

    # SOURCE_CHOICES = (
    #     ('YouTube', 'YouTube'),
    #     ('Google', 'Google'),
    #     ('Newsletter', 'Newsletter'),
    # )

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.PositiveIntegerField(default=0)
    organization =models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    agent = models.ForeignKey("Agent", null=True, blank=True, on_delete=models.SET_NULL) # When an agent is deleted the lead will be deleted as well

    category = models.ForeignKey("Category", null=True, blank=True, on_delete=models.SET_NULL)

    # phoned = models.BooleanField(default=False)
    # source = models.CharField(choices=SOURCE_CHOICES, max_length=100)

    # profile_picture = models.ImageField(blank=True, null=True)
    # special_files = models.FileField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.user.email    

class Category(models.Model):
    name = models.CharField(max_length=30, default="New") # New, Contacted, Converted, Unconverted
    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.name



def post_user_created_signal(sender, instance, created, **kwargs):
    #TODO Create a user profile
    print(instance, created)
    if created:
        UserProfile.objects.create(user=instance)
    # pass

post_save.connect(post_user_created_signal, sender=User)