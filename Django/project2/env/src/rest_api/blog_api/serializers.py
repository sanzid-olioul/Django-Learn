from rest_framework import serializers
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    height = serializers.CharField(max_length=8)
    weight = serializers.FloatField()
    institute = serializers.CharField(max_length=120)