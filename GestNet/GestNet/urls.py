# GestNet/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),
    path('clients/', include('clients.urls')),
    path('planning/', include('planning.urls')),
    path('execution/', include('execution.urls')),
    path('inspection/', include('inspection.urls')),
    path('documentation/', include('documentation.urls')),
    path('incidents/', include('incidents.urls')),
    path('employees/', include('employees.urls')),
    path('security/', include('security.urls')),
    path('client_portal/', include('client_portal.urls')),
]

