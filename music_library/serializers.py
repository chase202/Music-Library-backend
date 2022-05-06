from rest_framework import serializers
from .models import Song

class SongSerializer(Serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id','title','artist','album','release_date','genre']