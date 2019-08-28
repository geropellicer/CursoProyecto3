from rest_framework import serializers
from ebooks.models import Ebook, Review

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        # fields = "__all__"
        exclude = ('ebook',)

class EbookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ebook
        fields = "__all__"
