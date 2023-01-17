from django.urls import path
from .views import SnippetsListView, SnippetDetailView

urlpatterns = [
    path('snippets/', SnippetsListView.as_view()),
    path('snippets/<int:pk>/', SnippetDetailView.as_view()),
]
