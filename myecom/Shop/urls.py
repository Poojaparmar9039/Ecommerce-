from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('cartDetail/<int:id>/',views.cartDetail,name='cartDetail'),
    path('AddtoCart/<int:id>/',views.AddtoCart,name='AddtoCart'),
    path('wishlist/<int:id>/',views.wishlist,name='wishlist'),
    path('deletecart/<int:id>/',views.deletecart,name='deletecart'),
    path('deletelist/<int:id>/',views.deletelist,name='deletelist'),
    path('viewlist/',views.viewlist,name='viewlist'),
    path('viewcart/', views.viewcart, name='viewcart'),
    path('product_category/<str:category>/',views.product_category,name='product_category'),
    path('best_seller/',views.best_seller,name='best_seller'),
    path('shop/',views.shop,name='shop'),
    path('buy/<int:id>',views.buy,name='buy'),
    path('Address/',views.Address,name='Address'),
    path('addressDetail/',views.addressDetail,name='addressDetail'),
    path('payment/<int:id>/',views.payment,name='payment'),
    path('place_order/<int:id>',views.place_order,name='place_order'),
    path('place_order_cart/',views.place_order_cart,name='place_order_cart'),
    path('successful/',views.successful,name='successful'),
    path('order_update/',views.order_update,name='order_update'),
    path('search/',views.search,name='search'),

    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)