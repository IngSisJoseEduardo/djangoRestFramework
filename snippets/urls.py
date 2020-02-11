from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    SnippetList,
    SnippetDetail,
    UserList,
    UserDetail
)

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('snippets/', SnippetList.as_view()),
    path('snippets/<int:pk>/', SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns) # Permite poner el sufijo .api o .json para solciitar la respuesta