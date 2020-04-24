from django.shortcuts import render
from django.core import serializers
from .models import User
from django.forms.models import model_to_dict
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

#회원가입 /users/auth/

#아이디를 등록하는곳 /users/register
@api_view(['POST'])
def register(request):
    data=request.data
    if all(i in data for i in ('email','nickname','password')):
        email_check=User.objects.filter(email=data['email'])
        nick_check=User.objects.filter(nickname=data['nickname'])
        if email_check.exists():
            return Response({"message": "email already exists"}, status=status.HTTP_409_CONFLICT)
        elif nick_check.exists():
            return Response({"message": "nickname already exists"}, status=status.HTTP_409_CONFLICT)
        else:
            user = User.objects.create_user(
                data['email'],
                data['nickname'],
                data['password'],
            )
            user.save()
            return Response(model_to_dict(user), status=status.HTTP_201_CREATED)
    else:
        return Response({"message": "key error"}, status=status.HTTP_400_BAD_REQUEST)

# 토큰을 주면 해당 유저의 정보를 얻는 곳 /users/users
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def info(request):
    user = request.user
    data = request.data
    try:
        searchU=User.objects.filter(email=user.email)
        if searchU.count==0:
            return Response({"message": "Can't find info"}, status=status.HTTP_404_NOT_FOUND)
        data = {
            'email': user.email,
            'nickname':user.nickname
        }
        return Response((data), status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({"message": "info does not exists"}, status=status.HTTP_404_NOT_FOUND)

