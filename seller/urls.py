from django.urls import path
from.import views
app_name='seller'
urlpatterns=[
    path('seller_home/',views.seller_home ,name='seller_home'),
    path('seller_login/',views.seller_login,name='seller_login'),
    path('seller_dashboard/',views.seller_dashboard, name='seller_dashboard'),
    path('addproduct/', views.addproduct, name='addproduct'),
    path('view_products/', views.view_products, name='view_products'),
    path('delete_product/<int:product_id>', views.delete_product, name='delete_product'),
    path('update_product/<int:product_id>', views.update_product, name='update_product'),
    path('sellerlogout/',views.sellerlogout,name='sellerlogout')
    
]