from django.urls import path

from . import views

urlpatterns = [
    path('category/', views.CategoryList.as_view()),
    path('category/<int:pk>/', views.CategoryDetail.as_view()),
    path('board/', views.BoardList.as_view()),
    path('board/<int:pk>/', views.BoardDetail.as_view()),
]
