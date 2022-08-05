from django.urls import path

from accounts.views import login_view
from trecker.views import IndexView

app_name = "accounts"

urlpatterns = [
    path('login/', login_view, name="login"),


    ]
