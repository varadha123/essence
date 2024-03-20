from django.urls import path
from.import views
app_name='customer'
urlpatterns=[
    path('',views.Home, name='home'),
    path('signup/',views.signup, name='signup'),
    path('login/',views.login,name='login'),
    path('customer_dashboard/', views.customer_dashboard , name='customer_dashboard'),
    path('cart/',views.cart,name='cart'),
    path('add_to_cart/<int:product_id>',views.add_to_cart ,name='add_to_cart'),
    path('remove_from_cart/<int:product_id>',views.remove_from_cart, name='remove_from_cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('logout/',views.logout,name='logout'),
    path('search/',views.search,name='search')
]