from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
    path('function-secret/', views.secret_page, name='function-secret'),
    path('class-secret', views.SecretPage.as_view(), name='class-secret'),
]