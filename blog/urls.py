from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'blog'

urlpatterns = [
    path('', views.BlogIndexView.as_view(), name='index'),
    path('<int:pk>', views.BlogDetailView.as_view(), name='detail'),
    path('create/', views.BlogCreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.BlogUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.BlogDeleteView.as_view(), name='delete'),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
]
