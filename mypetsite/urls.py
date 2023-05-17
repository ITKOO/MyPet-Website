from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # 127.0.0.1:8000 로 들어오는 모든 접속 요청을 petsite.urls로 전송
    path('', include('petsite.urls')),
]
