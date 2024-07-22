from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

from posts.views import PostViewSet, CategoryViewSet
from mail.views import SubscriberViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'cats', CategoryViewSet)
router.register(r'subscribers', SubscriberViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)