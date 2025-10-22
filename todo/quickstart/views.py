from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

from .models import Task
from .serializers import TaskSerializer, GroupSerializer, UserSerializer


# -----------------------
# Usuários e grupos
# -----------------------
class UserViewSet(viewsets.ModelViewSet):
    """API endpoint que permite visualizar ou editar usuários"""
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class GroupViewSet(viewsets.ModelViewSet):
    """API endpoint que permite visualizar ou editar grupos"""
    queryset = Group.objects.all().order_by("name")
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]


# -----------------------
# Perfil do usuário logado
# -----------------------
class PerfilView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        user = request.user
        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email,
        })


# -----------------------
# CRUD de Tasks
# -----------------------
class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["completed", "data"]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


# -----------------------
# Registro de usuário via API
# -----------------------
@api_view(["POST"])
@permission_classes([AllowAny])
def register_user(request):
    username = request.data.get("username")
    password = request.data.get("password")

    if not username or not password:
        return Response(
            {"error": "Usuário e senha são obrigatórios"},
            status=status.HTTP_400_BAD_REQUEST
        )

    if User.objects.filter(username=username).exists():
        return Response(
            {"error": "Usuário já existe"},
            status=status.HTTP_400_BAD_REQUEST
        )

    user = User.objects.create_user(username=username, password=password)
    token = Token.objects.create(user=user)

    return Response(
        {"message": "Usuário criado com sucesso", "token": token.key},
        status=status.HTTP_201_CREATED
    )
