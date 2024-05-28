from .models import BooksLibrary

from rest_framework import serializers

class BooksLibrarySerializer(serializers.Serializer):
    Name = serializers.CharField(max_length=50)
    Price = serializers.IntegerField()
    Quantity = serializers.IntegerField()
    Author = serializers.CharField(max_length=50)
    Is_Publish = serializers.BooleanField(default=True)

    def create(self, validated_data):
        new_book = BooksLibrary.objects.create(**validated_data)
        return new_book
    
print("In main branch")