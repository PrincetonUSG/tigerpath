from django.urls import path
from . import views

urlpatterns = [
    # app urls
    path('', views.index, name='index'),
    path('landing', views.landing, name='landing'),
    path('about', views.about, name='about'),
    path('onboarding/save', views.save_onboarding, name='save_onboarding'),
    path('settings/save', views.save_user_settings, name='save_settings'),
    path('transcript', views.transcript, name='transcript'),
    # cas auth
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    # api
    path('api/v1/get_courses/<search_query>', views.get_courses, name='get_courses'),
    path('api/v1/update_schedule/', views.update_schedule, name='update_schedule'),
    path('api/v1/get_schedule/', views.get_schedule, name='get_schedule'),
    path('api/v1/get_requirements/', views.get_requirements, name='get_requirements'),
]
