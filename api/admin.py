from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Training)
admin.site.register(Coach)
admin.site.register(GroupTraining)
admin.site.register(TrainingUser)