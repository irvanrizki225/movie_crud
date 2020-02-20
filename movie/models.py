from django.db import models

# Create your models here.
class Movie(models.Model):
    judul = models.CharField(max_length = 80)
    genre = models.CharField(max_length = 80)
    year = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add = True) #ketika field diata di buat
    updated_at = models.DateTimeField(auto_now = True) #ketika field diata di buat
    creator = models.ForeignKey('auth.user', related_name = 'movie', on_delete = models.CASCADE)
    
