from django.contrib import admin
from django.urls import path, include

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', obtain_auth_token),
    path('', include('hacker_news.urls')),
    path('', include('news.urls')),
    path('', include('email_digest.urls')),
    path('', include('my_content.urls'))
]
