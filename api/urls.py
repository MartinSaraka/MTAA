from django.urls import path
from . import views


urlpatterns = [
    #path('admin/trainings/change/<int:id>', ),
    #path('admin/trainings/<int:id>', views.add_training),
    #path('admin/trainings', ),
    #path('admin/grouptrainings', ),
    path('users/register', views.add_user),
    #path('users/login', ),
    #path('trainigns/signup', ),
    #path('trainings', )
]
