from django.contrib import admin
from django.urls import path, include
from pythonapi.views import CommunautesView, CommunauteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('communautes/', CommunautesView),
    path('communaute/<int:nb>', CommunauteView),
]
