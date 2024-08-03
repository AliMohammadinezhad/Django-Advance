from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import PostSerializer, CategorySerializer
from .paginations import DefaultPagination
from .permissions import IsOwnerOrReadOnly

from ...models import Post, Category


class PostModelViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(status=True)
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["title", "content"]
    filterset_fields = {
        "category": ["exact", "in"],
        "author": ["exact"],
        "status": ["exact"],
    }
    ordering_fields = ["published_date"]
    pagination_class = DefaultPagination

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context


class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


"""
class PostViewSet(viewsets.ViewSet):
    queryset = Post.objects.filter(status=True)
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, *args, **kwargs):
        post_object = get_object_or_404(self.queryset, id=kwargs.get('pk'))
        serializer = self.serializer_class(post_object)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def update(self, request, *args, **kwargs):
        post_object = get_object_or_404(self.queryset, id=kwargs.get('pk'))
        serializer = self.serializer_class(post_object, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def partial_update(self, request, *args, **kwargs):
        post_object = get_object_or_404(self.queryset, id=kwargs.get('pk'))
        serializer = self.serializer_class(post_object, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        post_object = get_object_or_404(self.queryset, id=kwargs.get('pk'))
        post_object.delete()
        return Response({'detail':'post deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
 """


"""class PostListView(ListCreateAPIView):
    queryset = Post.objects.filter(status=True)
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]"""

"""class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.filter(status=True)
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    """


'''class PostListView(APIView):
    """Get a list of posts with get and post methods

    Args:
        APIView (GET, POST): get a list of posts with get and post methods
    """
    
    
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    
    def get(self, request, *args, **kwargs):
        """get a list of posts
        
        Returns:
            Response: return json list of posts 
        """
        posts = Post.objects.all()
        serializer = self.serializer_class(posts, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        """create a new post

        Returns:
            Response: create a new post with post method
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)'''

'''class PostDetailView(APIView):
    """GET, PUT, DELETE the post detail

    Args:
        APIView (View): Class Based View

    Returns:
        Response: Get, Edit and Delete the post detail 
    """
    permission_class = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    
    def get(self, request, pk):
        """Get Post Detail

        Args:
            request (HttpRequset): User Http Request
            pk (Primary Key): Id of the post

        Returns:
            Response: Json Response
        """
        post = get_object_or_404(Post, id=pk, status=True)
        serializer = self.serializer_class(post)
        return Response(serializer.data)
    
    def put(self, request, pk):
        """Edit Post Detail

        Args:
            request (HttpRequest): user request
            pk (Primary Key): Id Of the post

        Returns:
            Response: Http Response of the put
        """
        post = get_object_or_404(Post, id=pk, status=True)
        serializer = self.serializer_class(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk):
        """Delete Post Detail

        Args:
            request (HttpRequest): user request
            pk (Primary Key): Id of the detail Post

        Returns:
            Response: HttpResponse Message of State
        """
        post = get_object_or_404(Post, id=pk, status=True)
        post.delete()
        return Response({'detail':'post deleted successfully'}, status=status.HTTP_204_NO_CONTENT)'''


"""@api_view(['GET', 'POST'])
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exceptions=True)
        serializer.save()
        return Response(serializer.data)"""

"""@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, pk):
    post = get_object_or_404(Post, id=pk, status=True)
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    if request.method == 'DELETE':
        post.delete()
        return Response({'detail':'post deleted successfully'})"""
