from django.contrib.auth.models import User
from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer
from rest_framework import generics, permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Este conjunto de vistas proporciona automáticamente acciones de `lista` y` detalle`.
    """
    queryset         = User.objects.all()
    serializre_class = UserSerializer

class SnippetViewSet(viewsets.ModelViewSet):
    queryset            = Snippet.objects.all()
    serializer_class    = SnippetSerializer
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(Snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)