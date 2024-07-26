from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

####jwt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes 
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

####pagination
from django.core.paginator import Paginator

####MAIL
from django.core.mail import send_mail
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# Create your views here.

def test(request):
    person=Person.objects.all()
    paginator = Paginator(person, 5)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,'test.html',{'fm':person,'page_obj':page_obj})




@api_view(['GET'])
def getPerson(request):
    person=Person.objects.all()
    serializer=PersonSerializer(person,many=True)
    return Response({"message":"success","data":serializer.data})

@api_view(['POST'])
def getOne(request):
    fetch_id=request.data.get('id')
    person=Person.objects.get(pk=fetch_id)
    serializer=PersonSerializer(person)
    return Response({"message":"success","data":serializer.data})



@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add(request):
    requestData=request.data
    serializer=PersonSerializer(data=requestData)
    if serializer.is_valid():
        serializer.save()
    return Response({"message":"success","data":serializer.data})

@api_view(['POST'])
def update(request):
    id=request.data.get("id")
    person=Person.objects.get(pk=id)
    serializer=PersonSerializer(person,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
    return Response({"message":"success","data":serializer.data})

@api_view(['POST'])
def delete(request):
    id=request.data.get("id")
    person=Person.objects.get(pk=id)
    person.delete()
    return Response({"message":"success"})


