"""legal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from django.conf import settings
from django.conf.urls.static import static
#from .swagger_schema import SwaggerSchemaView

schema_view = get_swagger_view(title='Юр.Прайс API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web_page.urls')),
    path('api/v1/', include('category.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
from django.contrib import admin

admin.site.site_header = 'Панель Администратора'                    # default: "Django Administration"
admin.site.index_title = 'Панель Администратора'                 # default: "Site administration"
admin.site.site_title = 'lexprice'
