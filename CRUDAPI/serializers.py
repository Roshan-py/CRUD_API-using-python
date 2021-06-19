from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=1000)
    img = serializers.ImageField()
    summery = serializers.CharField(max_length=2000)

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.img=validated_data.get('img',instance.img)
        instance.summery=validated_data.get('name',instance.summery)
        instance.save()
        return instance


