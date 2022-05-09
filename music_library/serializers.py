from rest_framework import serializers
from .models import music_library

class Music_librarySerializer(serializers.ModelSerializer):
    class Meta:
        model = music_library
        fields = ['id','title','artist','album','release_date','genre']