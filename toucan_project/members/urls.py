from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Add this line
    path('add-member/', views.add_member, name='add_member'),
    path('member-list/', views.member_list, name='member_list'),
]
