from django.urls import path
from admin_dashboard import views
from admin_dashboard.admin_authentication import adminLogin
from plant_main import cart
from plant_main import wishlist
from plant_main.user_authentication import registerUser,loginUser,logoutUser
from plant_main import main_views

urlpatterns = [
    #admin-authentication
    path('admin-login', adminLogin, name='admin-login'),

    #admin-banner-category-plant-testimonial
    path('banner', views.banners, name='banners'),
    path('banner/<int:pk>', views.bannerMethod, name='banner_methods'),
    path('category', views.category, name='category'),
    path('category/<int:pk>', views.categoryMethod, name='category_methods'),
    path('plants', views.plants, name='plants'),
    path('plants/<int:pk>', views.plantMethod, name='plant_method'),
    path('testimonials', views.testimonials, name='testimonials'),
    path('testimonials/<int:pk>', views.testimonialMethod, name='testimonial_method'),

    #user-authentication
    path('user-register', registerUser, name='user_registration'),
    path('user-login', loginUser, name='user-login'),
    path('user-logout', logoutUser, name='user-logout'),

    #cart
    path('add-to-cart', cart.add_to_cart, name='add_to_cart'),
    path('view-cart', cart.viewCart, name='cart-list'),
    path('delete-cart-item/<int:pk>', cart.deleteCart, name='cart_item_delete'),
    path('update-cart-item-quantity', cart.update_cart_item_quantity, name='update_cart_item_quantity'),

    #wishlist
    path('add-to-wishlist', wishlist.add_to_wishlist, name='add_to_wishlist'),
    path('view-wishlist', wishlist.viewWishlist, name='wishlist-list'),
    path('delete-wishlist-item/<int:pk>', wishlist.deleteWishlist, name='wishlist_item_delete'),

    #main-views(product search, testimonial)
    path('search-product', main_views.plantSearch, name='search_product'),

]