from django.urls import path
from .views import home, detail, about
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views


urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:product_id>/', views.detail, name='detail'),
    path("about", views.about, name="about"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)