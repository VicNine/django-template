from snippets.models import Snippet
from snippets.api.serializers import SnippetSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView

####################################################################################################
####################################    Class-based API View    ####################################
####################################################################################################
class SnippetsListView(ListAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class SnippetDetailView(RetrieveAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer