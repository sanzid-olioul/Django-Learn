from rest_framework import serializers
from datetime import datetime
class BlogSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=250)
    author = serializers.CharField(max_length=50)
    content = serializers.CharField()
    created_at = serializers.DateTimeField(default=datetime.utcnow())