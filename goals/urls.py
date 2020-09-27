from django.urls import path, include
from .api import RegisterAPI, LoginAPI
from knox import views as knox_views
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    add_goals,
    get_all_goals,
    get_all_trackers,
    add_tracker,
    goals_for_user,
    trackers_for_goal
)

app_name = 'goals'
urlpatterns = [
    path('api/auth', include('knox.urls')),
    path('api/add_goals', add_goals, name='goals'),
    path('api/goals_for_user', goals_for_user, name='goals_for_user'),
    path('api/trackers_for_goal', trackers_for_goal, name='trackers_for_goal'),
    path('api/add_tracker', add_tracker, name='add_tracker'),
    path('api/all_goals', get_all_goals, name='all_goals'),
    path('api/all_trackers', get_all_trackers, name='all_trackers'),
    path('api/auth/logout', knox_views.LogoutView.as_view()),
    path('api/auth/register', RegisterAPI.as_view()),
    path('api/auth/login', LoginAPI.as_view(), name='login'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
