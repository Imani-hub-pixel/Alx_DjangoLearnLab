from .models import Book,Author
from  rest_framework import serializers
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=["__all__"]
    def validate(self,attrs):
        current_year=datetime.now().year
        pub_year=attrs.get("publication_year")


        if pub_year and pub_year > current_year:
            raise serializers.ValidationError(
                {"publication_year":"publication year cannnot be in the future"}
            )
        
        return attrs
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["__all__"]
    books = BookSerializer(many=True, read_only=True)

