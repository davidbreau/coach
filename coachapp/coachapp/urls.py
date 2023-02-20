"""coachapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import core.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core.views.index, name='index'),
    path('log_in/', core.views.log_in, name='log_in'),
    # path('', authentification.views.Login.as_view(), name='login'),
    path('sign_up/', core.views.sign_up, name='sign_up'),
    path('logout/', core.views.logout_user, name='logout'),
    path('rdv/', core.views.rdv, name='rdv'),
    path('about/', core.views.about, name='about'),
    path('seerdv/', core.views.seerdv, name='seerdv')
]
