from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('stonkcity/', include('stonkcity.urls')),
    path('admin/', admin.site.urls),
]
