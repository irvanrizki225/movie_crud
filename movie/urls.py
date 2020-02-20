from django.urls import include, path
from . import views


urlpatterns = [

    path('api/v1/movie/<int:pk>',
        views.get_delete_updete_movie.as_view(),
        name= 'get_delete_updete_movie',
    ),

    path('api/v1/movie',
        views.get_post_movie.as_view(),
        name = 'get_serializer'
    )

]
