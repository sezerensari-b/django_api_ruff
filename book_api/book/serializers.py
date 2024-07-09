from rest_framework import serializers
from .models import Book, BookSubject

class BookSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookSubject
        fields = ["name"]

class BookSerializer(serializers.ModelSerializer):
    subject = serializers.SlugRelatedField(slug_field='name', queryset=BookSubject.objects.all())

    class Meta:
        model = Book
        fields = ["title", "author", "page","subject"]