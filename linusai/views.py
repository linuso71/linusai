from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from rest_framework_simplejwt.tokens import RefreshToken
from django.views.decorators.csrf import csrf_exempt
# from api.models import Application_permission

@api_view(["POST"])
def register(request):
    email = request.data.get("email")
    name = request.data.get("name")
    password = request.data.get("password")
    # print(User.objects.get(email = email))
    # if User.objects.get(email = email):
    #     print(email)
    #     return Response("user already exists")
    User.objects.create(username=name,email= email, password = password)
    return Response({"name":name,"email":email})

@api_view(["POST"])
def user_login(request):
    username = request.data.get("name")
    password = request.data.get("password")
    print(username,password)
    email = User.objects.get(username = username).email
    print(email)
    auth  = authenticate(username = username,password = password)
    print(auth)
    login(request,auth)
    refresh  = RefreshToken.for_user(User.objects.get(username = username))
    access_token = str(refresh.access_token)
    # login(email = email, password = password)
    return Response({'output':{'user':username,'access_token':access_token}})

@api_view(["GET"])
def logout_user(request):
    logout(request)
    return Response({"successfully logout"})