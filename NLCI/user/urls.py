from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.welcome, name='jupiter is another planet'),
    path('user/members',views.members, name="another name"),
    path('user/first',views.first, name="another name"),
    path('user/child',views.testing, name="checking for masters and child"),
    path('user/add-employee', views.add_employee, name='add_employee'),
    path('master/<int:pk>/', views.master_detail_view, name='master-detail'),
    path('master/new/', views.master_detail_view, name='master-create'),
]
