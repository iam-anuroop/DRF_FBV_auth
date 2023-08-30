from rest_framework.decorators import api_view
from .models import Student
from .serializer import Studentserializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,permission_classes,authentication_classes


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def Student_apiview(request, pk=None):
    if request.method == 'GET':
        id = pk
        if pk is not None:
            stu = Student.objects.get(pk=id)
            serializer = Studentserializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = Studentserializer(stu, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = Studentserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created ...', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        id = pk
        stu = Student.objects.get(id=id)
        serializer = Studentserializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Updated ...', 'data': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        id = pk 
        stu = Student.objects.get(id=id)
        serializer = Studentserializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated ...', 'data': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        id = pk
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({'msg': 'Data deleted...'})
