from django.urls import path
from admin_dashboard import views

urlpatterns = [
    path('banner', views.banners, name='banners'),
    path('banner/<int:pk>', views.bannerMethod, name='banner_methods'),
    path('category', views.category, name='category_list'),
    path('category/<int:pk>', views.categoryMethod, name='category_methods'),
    path('plants', views.plants, name='plants'),
    path('plants/<int:pk>', views.plantMethod, name='plant_method')
]