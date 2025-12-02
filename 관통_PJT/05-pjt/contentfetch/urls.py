from django.urls import path
from . import views

app_name = 'contentfetch'
urlpatterns = [
    path('', views.stock_finder,name='stock_finder'),
    path('delete_comment/', views.delete_comment, name='delete_comment'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('profile/add/', views.add_stock, name='add_stock'),
    path('profile/delete/<int:stock_pk>/', views.delete_stock, name='delete_stock'),
    path('search/<str:stock_name>/', views.stock_finder, name='stock_finder_search'),
]
