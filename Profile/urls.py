from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from rest_framework import routers
from .views import ProfielViewSets

router = routers.DefaultRouter()
router.register('', ProfielViewSets)


app_name = 'Profile'


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html',authentication_form=LoginForm), name='login'),
    path('home/', views.profile_home, name='home'),
    path('profilelist/', views.ProfileListAPIView.as_view(), name='profilelist'),
    path('profiledetail/<int:pk>/', views.ProfileRetrieveAPIView.as_view(), name='profiledetail'),
    path('profileupdate/<int:pk>/', views.ProfileUpdateAPIView.as_view(), name='profileupdate'),
    path('profiledelete/<int:pk>/', views.ProfileDeleteAPIView.as_view(), name='profiledelete'),
    path('profiledetailupdate/<int:pk>/', views.ProfileDetailUpdateAPIView.as_view(), name='profiledetailupdate'),
    path('profilecreate', views.ProfileCreateApIView.as_view(), name='profilecreate'),
    path('profileviewsets/', include(router.urls)),
    path('profileAPIView/', views.ProfileAPIView.as_view(), name='profileAPIView'),
]
