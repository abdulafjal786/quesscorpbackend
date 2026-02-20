"""
URL configuration for quesscorpbackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include,re_path

from django.views.generic import TemplateView
from django.views.static import serve
from django.conf import settings
import os

BASE_OUT = os.path.join(settings.BASE_DIR, "out")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('employee/', include('employee.urls')),
    
    
       # Serve Next.js _next static assets
    re_path(r'^_next/(?P<path>.*)$', serve, {'document_root': os.path.join(BASE_OUT, '_next')}),

    # Specific static pages
    path('employee/', TemplateView.as_view(template_name=os.path.join(BASE_OUT, 'employee.html'))),
    path('attendance/', TemplateView.as_view(template_name=os.path.join(BASE_OUT, 'attendance.html'))),

    # Catch-all -> index.html
    re_path(r'^.*$', TemplateView.as_view(template_name=os.path.join(BASE_OUT, 'index.html'))),
]
