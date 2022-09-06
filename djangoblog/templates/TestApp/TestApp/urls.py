
from django.contrib import admin
from django.urls import path
from TestApp2.views import  Login
from TestApp2.views import Data
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',Login),
    path('login/data/',Data)
]
