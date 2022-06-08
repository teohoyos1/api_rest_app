from django.urls import path
from product import views

urlpatterns = [
    path('', views.ProductListCreateAPIView.as_view()), #views.product_alt_view
    path('<int:pk>/',views.ProductDetailAPIView.as_view()), #views.product_alt_view
    path('<int:pk>/update/', views.ProductUpdateAPIView.as_view()),
    path('<int:pk>/delete/', views.ProductDestroyAPIView.as_view()),
]
