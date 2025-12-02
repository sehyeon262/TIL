from django.urls import path
from . import views

app_name = 'crawlings'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('stocks/<int:pk>/delete/', views.delete, name='delete'),
    path('stocks/<int:stock_id>/comments/<int:idx>/delete/',
         views.delete_comment, name='delete_comment'),
]
