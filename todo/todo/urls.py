from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views as drf_views
from quickstart import views
from django.contrib.auth import views as auth_view

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),

    # Login e logout do Django (apenas se quiser acessar painel web)
    path(
        "",
        auth_view.LoginView.as_view(
            template_name="quickstart/login.html",
            redirect_authenticated_user=True,
        ),
        name="login",
    ),
    path("logout/", auth_view.LogoutView.as_view(next_page="/"), name="logout"),

    # 🔹 Registro via API (para app mobile)
    path("api/register/", views.register_user, name="api_register"),

    # 🔹 Login por token (para app mobile)
    path("api/token/", drf_views.obtain_auth_token, name="api_token_auth"),

    # 🔹 Rotas da API de tasks
    path("api/tasks/", include("quickstart.urls")),

    # 🔹 Endpoint individual de task (opcional, pode ser acessado via quickstart/urls)
    path("tasks/<int:pk>/", views.TaskDetailView.as_view(), name="task-detail"),

    # API do Django Rest Framework (interface web)
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
