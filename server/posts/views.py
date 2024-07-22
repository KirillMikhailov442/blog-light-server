from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters


from .models import Post, Category
from .serializer import PostSerializer, CategorySerializer

class PostViewSetPagination(PageNumberPagination):
    page_size = 8
    page_query_param = 'list_index'
    max_page_size = 100


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostViewSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'cat__name']

    
class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
