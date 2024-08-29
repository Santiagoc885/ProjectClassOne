
from django.urls import path
from .views import (
    login,
    home,
    app
)

app_name = 'authentication'

urlpatterns = [
    path('', home.home, name='home'),
    path('app/', app.app, name='app'),
    path('login/', login.user_login, name='user_login'), 
    # path('logout/', login.LogoutView.as_view(), name='logout'), 
]
