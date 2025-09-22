from rest_framework import viewsets, permissions, generics
from .models import Task
from .serializers import TaskSerializer, RegisterSerializer

# Register new users
class RegisterView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

# Task CRUD for logged-in users
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).order_by("-created_at")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
