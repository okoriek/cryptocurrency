from django.urls import path
from .import views
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)




urlpatterns = [
    path('password_reset/', PasswordResetView.as_view(template_name='password/reset_password.html'), name='reset_password'),
    path('password_reset_done/', PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='password/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'), name='password_reset_complete'),

    path('login/', LoginView.as_view(template_name='crypto/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='crypto/logout.html'), name='logout'),

    path('password_change/', views.passwordreset ,name='passwordreset'),
    path('contract/', views.Contract, name='contract'),
    path('home/', views.home, name='home'),
    path('register/', views.Register, name='register'),
    path('register/<str:ref_code>/', views.Register, name='register'),
    path('Profile-dashboard/', views.Dashboard, name='dashboard'),
    path('verification/', views.email, name='email'),
    path('activate/', views.Activate, name='activate'),
    path('Profile-details/', views.profiledetails, name='profiledetails'),
    path('history/', views.HistoryViews, name='history'),
    path('checkview', views.checkview, name='checkview'),
    path('<str:room>/', views.room, name='room'),
    path('live_chat', views.confirmation, name='check'),
    path('send', views.send, name='send'),
    path('receive/<str:room>/', views.receive, name='receive')
] 