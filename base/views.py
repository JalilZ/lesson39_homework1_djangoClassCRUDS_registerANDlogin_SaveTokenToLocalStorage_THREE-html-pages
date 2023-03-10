from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .serializers import StudentSerializer       # CRUD for Vicky
from .models import Student                      # CRUD for Vicky
from rest_framework.response import Response     # CRUD for Vicky
from rest_framework.decorators import api_view   # CRUD for Vicky (api_view)

from rest_framework.views import APIView         # django4kids: from rest_framework.views import APIView (views.py using class and CRUD methods in that class)
from rest_framework import status                # better to use with response (better practice), instead of writing a sentence lets say "student was added"
# making CRUDS with a class is better, we can copy paste it to make a new CRUD for a new model (lets say Product)

from rest_framework_simplejwt.views import TokenObtainPairView   # Authentication
from rest_framework.decorators import permission_classes         # Authentication (permission_classes)
from rest_framework.permissions import IsAuthenticated           # Authentication (permission_classes)  

def index(req):
    return JsonResponse('Nothing to see here... go to /students !', safe=False) #safe=False parameter is used to allow the response to be a plain Python object, rather than requiring it to be a dictionary. This is useful when returning simple responses like strings or numbers.

@api_view(['GET'])
def index1(req):
    return Response('Nothing to see here also... go to /students !')

@permission_classes([IsAuthenticated])                  # Authentication (permission_classes) 
class StudentModelView(APIView):
    """
    This class handle the CRUD operations for Student Model
    """
    def get(self, request, id=-1):
        if id > -1:
            try:
                stu = Student.objects.get(id=id)
                stu_serialized = StudentSerializer(stu, many=False) 
                return Response(stu_serialized.data)
            except Student.DoesNotExist:
                return Response('Student Does Not Exist!!!!!!!', status=status.HTTP_204_NO_CONTENT)
        else:
            stu = Student.objects.all()
            stu_serialized = StudentSerializer(stu, many=True) 
            return Response(stu_serialized.data)
        
    def post(self, request):
        stu = StudentSerializer(data=request.data)
        if stu.is_valid():
            stu.save()
            #stu_name = stu.data.get('name') # get is a method from .serializers () along with update copy clear .....
            #return Response (f'Student {stu_name} was added') # works, but better to use status (can be used with Response)
            return Response(stu.data, status=status.HTTP_201_CREATED)
        else:
            return Response(stu.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, id): # we couldve also used the update() (see below req.method == 'POST'), same shit... update() is same is instansiating StudentSerializer & save()
        old_stu = Student.objects.get(id=id)
        new_stu_serialized = StudentSerializer(old_stu ,data=request.data)
        if new_stu_serialized.is_valid():
            new_stu_serialized.save()
            return Response(new_stu_serialized.data, status=status.HTTP_201_CREATED)
        else:
            return Response(new_stu_serialized.data, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        stu = Student.objects.get(id=id)
        stu_name = stu.name
        stu.delete()
        return Response(f'Student {stu_name} was deleted.', status=status.HTTP_204_NO_CONTENT)

# Register (django4kids)
from django.contrib.auth.models import User # we import this class model (in django there is already a built in table/model called auth_user)

@api_view(['POST'])
def register(request):
    user = User.objects.create_user(             # use create_user method and not create ! (create password would be not encrypted!)
                username=request.data['username'],
                email=request.data['email'],
                password=request.data['password']
            )

    user.is_active = True
    user.is_staff = True
    user.save()
    return Response("new user born")

###Below using api_view (CRUDS for Vicky) - old way.

#@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
#def students(req, id=-1):
#    if req.method == 'GET':
#        if id > -1:
#            try:
#                stu = Student.objects.get(id=id)
#                return Response(StudentSerializer(stu,many=False).data)
#                #return Response({'id': stu.id, 'name': stu.name, 'age': stu.age, 'createdTime': stu.createdTime, 'image': f'/images{stu.image}'})
#            except Student.DoesNotExist:
#                return Response('Not Found')
#
#        all_students = StudentSerializer(Student.objects.all(), many=True).data
#        return Response(all_students)
#    
#    elif req.method == 'DELETE':
#        try:
#            stu = Student.objects.get(id=id)
#        except Student.DoesNotExist:
#            return Response('Not Found')
#        temp_name = Student.objects.get(id=id).name
#        stu.delete()
#        return Response(f'Student {temp_name} was deleted.')
#    
#    elif req.method == 'POST':
#        stu = StudentSerializer(data=req.data)
#        if stu.is_valid():
#            stu.save()
#            stu_name = stu.data.get('name') # get is a method from .serializers () along with update copy clear .....
#            return Response (f'Student {stu_name} was added')
#        else:
#            return Response(stu.errors)
#        
#    elif req.method == 'PUT' or req.method == 'PATCH':
#        try:
#            stu = Student.objects.get(id=id)
#        except Student.DoesNotExist:
#            return Response('Student was not Found')
#        
#        new_stu = StudentSerializer(req.data)
#        old_stu  = Student.objects.get(id=id)
#        res = new_stu.update(old_stu, req.data)
#        return Response(StudentSerializer(res,many=False).data)




