from django import admin
from django import static
from django import path, include
from django import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
