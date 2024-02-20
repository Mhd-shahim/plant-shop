from django.urls import path
from admin_dashboard import views
from admin_dashboard.admin_authentication import adminLogin


urlpatterns = [
    #admin-authentication
    path('admin-login', adminLogin, name='admin-login'),
    path('banner', views.banners, name='banners'),
    path('banner/<int:pk>', views.bannerMethod, name='banner_methods'),
    path('category', views.category, name='category_list'),
    path('category/<int:pk>', views.categoryMethod, name='category_methods'),
    path('plants', views.plants, name='plants'),
    path('plants/<int:pk>', views.plantMethod, name='plant_method')
]