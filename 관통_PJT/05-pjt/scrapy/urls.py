from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('pjt05/admin/', admin.site.urls),
    path('pjt05/', include('contentfetch.urls')),
    # 로그인 URL
    path('pjt05/login/', auth_views.LoginView.as_view(template_name='contentfetch/login.html'), name='login'),
    # 로그아웃 URL
    path('pjt05/logout/', auth_views.LogoutView.as_view(), name='logout'),
]