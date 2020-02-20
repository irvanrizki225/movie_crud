from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Movie
from .permissions import IsOwnerOrReadOnly
from .serializers import MovieSerializer
# from .pagination import CostomPagination



class get_delete_updete_movie(RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    renderer_classes = [JSONRenderer]


    def get_queryset(self, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            content = {
                'status':'not found'
            }
            return Response(content, status= status.HTTP_404_NOT_FOUND)
        return movie

    #get movie
    def get(self, request, pk):

        movie = self.get_queryset(pk)
        serializer = MovieSerializer(movie, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    #update movie
    def put(self, request, pk):
        movie = self.get_queryset(pk)

        if (request.user == movie.creator):
            serializer = MovieSerializer(movie, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        else:
            content = {
                'status':'unauthorized'
            }
            Response(content, status = status.HTTP_401_UNAUTHORIZED)
            return Response

    #delete movie
    def delete(self, request, pk):

        movie = self.get_queryset(pk)

        if(request.user == user.creator):
            movie.delete()
            content = {
                'status':'No Content'
            }
            return Response(content, status = status.HTTP204_NO_CONTENT)
        else:
            content = {
                'status':'UNAUTHORIZED'
            }
            return Response(content, status = status.HTTP_401_UNAUTHORIZED)


class get_post_movie(ListCreateAPIView):
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticated)
    renderer_classes = [JSONRenderer]

    # pagination_class = CustomPagination

    def get_queryset(self):
        movie = Movie.Objects.all()
        serializer = MovieSerializer(movie, many=True)
        return movie

    #mengambil semua oject movie
    def get(self, request):
        movie = self.get_queryset()
        # paginate_queryset = self.paginate_queryset(movie)
        # serializer = self.serializer_class(paginate_queryset, many = True)
        serializer = MovieSerializer(movie, many=True)
        return Response(serializer.data)

    #membuat baru movie
    def post(self, request):
        serializer = MovieSerializer
        if serializer.is_valid():
            serializers.save(creator = request.user)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
