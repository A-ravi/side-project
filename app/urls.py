from django.urls import path, include

from . import views

urlpatterns = [
    path('<int:table_no>', views.index, name='index'),
    path('order', views.order, name='order'),
    path('orderMore', views.orderMore, name='orderMore'),
    path('admin', views.adminLogin, name='adminLogin'),
    path('admin/dashboard', views.adminDashboard, name='adminDashboard'),
]
