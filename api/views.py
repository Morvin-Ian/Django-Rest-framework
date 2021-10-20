from django.shortcuts import render
from .serializers import StudentSerializer
from django.http import JsonResponse,HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Student

from rest_framework.views import APIView
 
#generics and mixins for Generic views 
from rest_framework import generics
from rest_framework import mixins

#Authentication
from rest_framework.authentication import SessionAuthentication,TokenAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated

#Viewsets
from rest_framework import viewsets
from django.shortcuts import get_object_or_404



# When the commented lines are used, the uncommented ones should be commented/removed


#function based
# 1)Normal functions

@csrf_exempt
def student_list(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many= True)
        return JsonResponse(serializer.data, safe=False)
       

    elif request.method == 'POST':
        student = JSONParsers().parse(request)
        serializer = StudentSerializer(data=request.data)
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.error, status = 400)
         

@csrf_exempt
def details(request,pk):
    try:
        student = Student.objects.get(pk=pk)
    except Sudent.DoesNotExist:
        return HttpResponse(status = 404)
       

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return JsonResponse(serializer.data)
      

    elif request.method == 'PUT':
        student = JSONParsers().parse(request)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.error, status = 400)
           

    elif request.method == 'DELETE':
        student.delete()
        return HttpResponse(status = 204)
       





# 2) api_view decorator     
@api_view(['POST','GET'])
def student_list(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many= True)
        return JsonResponse(serializer.data, safe=False)
     

    elif request.method == 'POST':
        student = JSONParsers().parse(request)
        serializer = StudentSerializer(data=request.data)
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.error, status = 400)
      

@api_view(['GET','PUT','DELETE'])
def details(request,pk):
    try:
        student = Student.objects.get(pk=pk)
    except Sudent.DoesNotExist:
        return HttpResponse(status = 404)
      

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return JsonResponse(serializer.data)
       

    elif request.method == 'PUT':
        student = JSONParsers().parse(request)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.error, status = 400)
       

    elif request.method == 'DELETE':
        student.delete()
        return HttpResponse(status = 204)
       





#class based
class StudentApiView(APIView):
    def get(self,request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many= True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class StudentDetailApi(APIView):
    def details(self,pk):
        try:
            return Student.objects.get(pk=pk)
        except Sudent.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        student=self.details(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student=self.details(pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        student=self.details(pk)
        student.delete()
        return Response(status =status.HTTP_204_NO_CONTENT)






#generic views and mixins
class StudentGenericView(generics.GenericAPIView, mixins.ListModelMixin,mixins.CreateModelMixin,
                        mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    lookup_field = 'pk'

    # #Basic authentication
    authentication_classes = [SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    #Token authentication
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self,request,pk=None):

        if pk:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self,request):
        return self.create(request)
    
    def put(self,request,pk=None):
        return self.update(request,pk)

    def delete(self,request,pk):
        return self.destroy(request,pk)





#Viewsets and routers
class StudentViewset(viewsets.ViewSet):
    def list(self,request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many= True)
        return Response(serializer.data)

    def create(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def  retrieve(self,request,pk=None):
        queryset = Student.objects.all()
        student = get_object_or_404(queryset,pk=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data) 

    def update(self, request,pk=None):
        student= Student.objects.get(pk=pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)





#Generic viewsets
class ArticleGenericViewset(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin,
    mixins.DestroyModelMixin, mixins.RetrieveModelMixin,mixins.UpdateModelMixin):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    lookup_field = 'pk'