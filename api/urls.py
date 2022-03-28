from django.urls import path
from . import views


urlpatterns = [
    #path('admin/trainings/change/<int:id>', ),
    path('admin/trainings/<int:id>', views.delete_training),
    path('admin/trainings', views.add_training),
    path('admin/grouptrainings', views.put_grouptraining),
    path('users/register', views.user_register),
    path('users/login', views.user_login),
    path('trainings/signup', views.training_user),
    path('trainings',views.get_trainings),
    path('trainings/grouptrainings', views.get_grouptraining)
]
