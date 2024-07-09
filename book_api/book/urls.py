from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns


from .views import (
    BookApiView,
    BookDetailApiView,
    BookSubjectApiView,
    BookSubjectDetailApiView,
)

urlpatterns = [
    path("books/", BookApiView.as_view(), name="book-list"),
    path("books/<int:pk>/", BookDetailApiView.as_view(), name="book-detail"),
    path("book-subjects/", BookSubjectApiView.as_view(), name="book-subject-list"),
    path(
        "book-subjects/<int:pk>/",
        BookSubjectDetailApiView.as_view(),
        name="book-subject-detail",
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
