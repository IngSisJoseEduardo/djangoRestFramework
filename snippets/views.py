from django.contrib.auth.models import User
from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer
from rest_framework import generics, permissions
from .permissions import IsOwnerOrReadOnly

class UserList(generics.ListAPIView):
    """
    Lista todos los usuarios utilizando el serializer de User que incluye la relacion de snippets
    """
    queryset         = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    """
    Muestra el detalle de un usuario
    """
    queryset = User.objects.all()
    serializer_classs = UserSerializer

class SnippetList(generics.ListCreateAPIView):
    """
    Lista y crea fragemntos de codigo
    """
    queryset           = Snippet.objects.all()
    serializer_class   = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Muestra, actualiza y elimina un fragmento de codigo
    """
    queryset           = Snippet.objects.all()
    serializer_class   = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]