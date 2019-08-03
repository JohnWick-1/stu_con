"""consumer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls import url
from consumerapp.views import StudentConViewSet
from consumerapp import views

schema_view = get_swagger_view(title='Consumer API')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('con/',include('consumerapp.urls')),
    path('view/',StudentConViewSet),
    url(r'swag/',schema_view),
    path('home/',views.home),
    path('home/save/',views.student_save),
    path('home/delete/<int:id>',views.delete),
    path('home/on/<int:id>',views.on),
    path('home/update/<int:id>',views.update),

    path('get/<int:id>',views.test2),
    path('getall/',views.test1),
    path('delete/<int:id>',views.test3)

]
