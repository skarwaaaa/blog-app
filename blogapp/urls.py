from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from posts import views


urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', include('posts.urls')),
    path('admin/', admin.site.urls),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
