from rest_framework import serializers
from tt.models import Post


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'post_title',
            'post_text',
            'pub_date',
        )
        model = Post
