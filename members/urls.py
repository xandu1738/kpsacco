from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('signup/', views.registerPage, name='signup'),
    # path('login/', views.login, name='login'),
    path('register/', views.join_sacco, name='register'),
    path('create-sacco/', views.create_sacco, name='create_sacco'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('roster/', views.roster, name='roster'),
    path('paid/', views.paid, name='paid'),
    path('unpaid/', views.unpaid, name='unpaid'),
    path('update_status/<str:pk>/', views.update_list, name='update_status'),

]
