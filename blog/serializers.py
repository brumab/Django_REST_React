from rest_framework import serializers
from .models import Blog, comentario

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = comentario
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    comentario = ComentarioSerializer(many=True, read_only=True)
    class Meta:
        model = Blog
        fields =  '__all__'


