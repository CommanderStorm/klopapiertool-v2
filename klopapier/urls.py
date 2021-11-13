from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.generic import RedirectView

urlpatterns = [
    # Auth
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    # localization
    path("i18n/", include("django.conf.urls.i18n")),
    # Views
    path("common/", include("common.urls")),
    # Admin
    path("admin/", admin.site.urls),
    # Index
    path("", RedirectView.as_view(pattern_name="common:dashboard"), name="main-view"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
