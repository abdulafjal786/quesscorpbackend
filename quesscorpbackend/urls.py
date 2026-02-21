from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.views.static import serve
from django.conf import settings
import os

BASE_OUT = os.path.join(settings.BASE_DIR, "out")

urlpatterns = [
    path('admin/', admin.site.urls),

    # API routes
    path('api/accounts/', include('accounts.urls')),
    path('api/employee/', include('employee.urls')),

    # Serve Next.js _next static files
    re_path(r'^_next/(?P<path>.*)$',
            serve,
            {'document_root': os.path.join(BASE_OUT, '_next')}),

    path('', TemplateView.as_view(template_name='index.html')),
    # path('employee/', TemplateView.as_view(template_name='employee.html')),
    path('attendance', TemplateView.as_view(template_name='attendance.html')),
    path('employee', TemplateView.as_view(template_name='employee.html')),
]