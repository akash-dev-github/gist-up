from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import status

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


def login_view(request):
    template = 'loginPage.html'
    return render(template)


@api_view(['POST'])
def sign_in(request):
    """
        sign-in API

        email -- email
        password -- password

    """

    email = request.data.get('email')
    if not email:
        return Response({'success': False, 'message': 'email mandatory.'}, status=status.HTTP_403_FORBIDDEN)
    password = request.data.get('password')
    if not password:
        return Response({'success': False, 'message': 'Password mandatory.'}, status=status.HTTP_403_FORBIDDEN)

    user = authenticate(username=email, password=password)
    if user is not None:  # password verified for the user
        if user.is_active:
            login(request, user)
            return Response({'success': True, 'login_url': ''}, status=status.HTTP_200_OK)
        else:
            return Response({'success': False, 'message': 'User not active.'}, status=status.HTTP_403_FORBIDDEN)
    else:  # the authentication system was unable to verify the username and password
        return Response({'success': False, 'message': 'User not found.'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def sign_up(request):
    """
        sign-up API

        email -- email-id
        password -- password

    """

    email = request.data.get('email')
    if not email:
        return Response({'success': False, 'message': 'email mandatory.'})
    password = request.data.get('password')
    if not password:
        return Response({'success': False, 'message': 'Password mandatory.'})
    username = email

    try:
        user = User.objects.create_user(username, email, password)
        # user.is_active = False
        # user.save()
    except:
        return Response({'success': False, 'message': 'User Sign-up failed. Try another username.'},
                        status=status.HTTP_400_BAD_REQUEST)

    return Response({'success': True}, status=status.HTTP_201_CREATED)


@api_view()
def logout_view(request):
    """
    logout a user
    """
    logout(request)
    return Response({'success': True}, status=status.HTTP_200_OK)


