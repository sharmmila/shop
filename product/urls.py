from django.urls import path
from product import views

urlpatterns = [
    path('', views.CategoryListCreateAPIView.as_view()),
    path('<int:id>/', views.CategoryDetailAPIView.as_view()),
    path('', views.ProductListCreateAPIView.as_view()),
    path('<int:id>/', views.ProductDetailAPIView.as_view()),
    path('<int:id>/', views.ReviewDetailAPIView.as_view()),
    path('', views.ReviewListCreateAPIView.as_view())
]