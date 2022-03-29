from django.urls import path
from . import views


urlpatterns = [
    path('admin/<str:player_token>/trainings/change/<int:id>', views.put_training),
    path('admin/<str:player_token>/trainings/<int:id>', views.delete_training),
    path('admin/<str:player_token>/trainings', views.add_training),
    path('admin/<str:player_token>/grouptrainings', views.put_grouptraining),
    path('users/register', views.user_register),
    path('users/login', views.user_login),
    path('<str:player_token>/trainings/signup', views.training_user),
    path('<str:player_token>/trainings',views.get_trainings),
    path('<str:player_token>/trainings/grouptrainings', views.get_grouptraining)
]