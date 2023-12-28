from rest_framework import serializers 
from .models import Post
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'bode', 'created_at', 'updated')

    def update(self, instance, validated_data):
        """
        Update and return an existing `Post` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.bode = validated_data.get('bode', instance.bode)
        instance.save()
        return instance