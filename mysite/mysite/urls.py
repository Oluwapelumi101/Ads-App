import os
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.views.static import serve
from django.views.generic import TemplateView
from django.conf.urls.static import static

urlpatterns = [
    path("ads/", include("ads.urls")),  # Change to ads.urls
    path("", TemplateView.as_view(template_name="home/main.html")),
    path("admin/", admin.site.urls),  # Keep
    path("accounts/", include("django.contrib.auth.urls")),  # Keep
    re_path(r"^oauth/", include("social_django.urls", namespace="social")),  # Keep
]

urlpatterns += [
    path(
        "favicon.ico",
        serve,
        {
            "path": "favicon.ico",
            "document_root": os.path.join(settings.BASE_DIR, "home/static"),
        },
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Switch to social login if it is configured - Keep for later
try:
    from . import github_settings

    social_login = "registration/login_social.html"
    urlpatterns.insert(
        0,
        path(
            "accounts/login/", auth_views.LoginView.as_view(template_name=social_login)
        ),
    )
    # print('Using', social_login, 'as the login template')
except:
    # print('Using registration/login.html as the login template')
    pass
