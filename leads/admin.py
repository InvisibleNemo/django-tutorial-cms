from curses.ascii import US
from django.contrib import admin

# Register your models here.

from .models import User, Lead, Agent, UserProfile, Category

admin.site.register(Category)
admin.site.register(User)
admin.site.register(Lead)
admin.site.register(Agent)
admin.site.register(UserProfile)