from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Book, BookSubject
from .serializers import BookSerializer, BookSubjectSerializer
 
class BaseAPIView(APIView):
    model = None
    serializer_class = None

    #List all
    def get(self, request):
        '''
        List all objects
        '''
        objects = self.model.objects.all()
        serializer = self.serializer_class(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    #Create
    def post(self, request):
        '''
        Create new object
        '''
        model_fields = [field.name for field in self.model._meta.get_fields() if field.name != 'id']
        
        data = {}
        for field_name in model_fields:
            if field_name in request.data:
                data[field_name] = request.data[field_name]
        
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BaseDetailAPIView(APIView):
    model= None
    serializer_class= None

    def get_object(self, pk):
        '''
        Helper method
        '''
        try:
            return self.model.objects.get(id=pk)
        except self.model.DoesNotExist:
            return None
        
    #List One
    def get(self, request, pk):
        '''
        Get object with given id
        '''
        instance = self.get_object(pk)

        if not instance:
            return Response(
                {"res": "Object with given id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = self.serializer_class(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    #Update
    def put(self, request, pk):
        '''
        Update object with given id
        '''
        instance = self.get_object(pk)

        if not instance:
            return Response(
                {"res": "Object with given id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        model_fields = [field.name for field in self.model._meta.get_fields() if field.name != 'id']
        
        data = {}
        for field_name in model_fields:
            if field_name in request.data:
                data[field_name] = request.data[field_name]

        serializer = self.serializer_class(instance= instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #Delete
    def delete(self, request, pk):
        '''
        Delete object with given id
        '''
        instance = self.get_object(pk)

        if not instance:
            return Response(
                {"res": "Object with given id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        instance.delete()
        return Response(
            {"res": "Object deleted."},
            status=status.HTTP_200_OK
        )

class BookApiView(BaseAPIView):
    model = Book
    serializer_class = BookSerializer

class BookSubjectApiView(BaseAPIView):
    model = BookSubject
    serializer_class = BookSubjectSerializer

class BookDetailApiView(BaseDetailAPIView):
    model = Book
    serializer_class = BookSerializer
   
class BookSubjectDetailApiView(BaseDetailAPIView):
    model = BookSubject
    serializer_class = BookSubjectSerializer