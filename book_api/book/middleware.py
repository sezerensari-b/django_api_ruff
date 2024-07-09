from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response


class CustomExceptionHandlerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        if isinstance(exception, ObjectDoesNotExist):
            return Response(
                {"res": "Object with given id does not exist"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        # Handle other exceptions if needed
        return None
