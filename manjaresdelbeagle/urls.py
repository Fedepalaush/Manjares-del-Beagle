"""manjaresdelbeagle URL Configuration

The `urlpatterns` list routes URLs to View. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function View
    1. Add an import:  from my_app import View
    2. Add a URL to urlpatterns:  path('', View.home, name='home')
Class-based View
    1. Add an import:  from other_app.View import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rotiseria.urls')),
]
