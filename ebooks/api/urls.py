from django.urls import path
from ebooks.api.views import (EbookListCreateAPIView, EbookDetailAPIView,
                                ReviewCreateAPIView, ReviewDetailAPIView)

urlpatterns = [
    path('ebooks/', EbookListCreateAPIView.as_view(), name='ebook-list'),
    path('ebooks/<int:pk>', EbookDetailAPIView.as_view(), name='ebook-details'),
    path('ebooks/<int:ebook_pk>/review', ReviewCreateAPIView.as_view(), name='create-review'),
    path('reviews/<int:pk>', ReviewDetailAPIView.as_view(), name='review-details'),
]