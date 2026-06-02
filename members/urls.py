from django.urls import path
from . import views

urlpatterns = [

    path('', views.register_member, name='register_member'),

    path('members/', views.member_list, name='member_list'),

    path('print/<int:pk>/', views.print_member, name='print_member'),
]