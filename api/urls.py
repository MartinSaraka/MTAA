from django.urls import path
from . import views


urlpatterns = [
    #path('admin/trainings/change/<int:id>', ),
    #path('admin/trainings/<int:id>', views.add_training),
    path('admin/trainings', views.add_training),
    #path('admin/grouptrainings', ),
    path('users/register', views.user_register),
    path('users/login', views.user_login),
    #path('trainigns/signup', ),
    #path('trainings', )
]
