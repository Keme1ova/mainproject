from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('home.urls')),
	path('', include('service.urls')),
	path('', include('comment.urls')),
	path('', include('book.urls')),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
