from django.urls import path

from . import views

app_name = 'user'

urlpatterns = [
    # api/user/create/ etc... from app.urls (app > urls.py)
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
]
