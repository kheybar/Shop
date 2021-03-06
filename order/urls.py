from django.urls import path
from . import views



app_name = 'order'
urlpatterns = [
    path('create/', views.OrderCreate.as_view(), name='order_create'),
    path('<int:order_id>/', views.OrderDeteil.as_view(), name='order_detail'),
    path('coupon-apply/<int:order_id>/', views.couponapply, name='coupon_apply'),
    path('payment/<int:order_id>/<int:price>/', views.payment, name='payment'),
    path('verify/', views.verify, name='verify'),
]