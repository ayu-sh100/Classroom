
from rest_framework.response import Response
from django.http import HttpResponse
from . serializers import CustomUserSerializer
from . models import CustomUser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail
from django.template.loader import render_to_string

def send_welcome_email(email):
    subject = 'Welcome to KIIT University.!'
    message = 'Thank you for registering with us!'
    from_email = 'ayush.a.brudite@gmail.com'
    recipient_list = [email]
    html_message = render_to_string('index.html', {})
    send_mail(subject, message, from_email, recipient_list, html_message=html_message)

class RegisterApi(APIView):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        data = request.POST
        serializer = CustomUserSerializer(data=data)
        if serializer.is_valid():
            user=serializer.save()
            send_welcome_email(user.email)
            return redirect('login')
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def get(self, request):
        return render(request, 'login.html')
    def post(self, request, format=None):
        email = request.data.get('email')
        password = request.data.get('password')
        # email = request.POST['email']
        # password = request.POST['password']
        user = authenticate(request,email=email, password=password)
        if user is not None:
            # User is authenticated
            # You can either create a new token for the user or use an existing token
            token, _ = Token.objects.get_or_create(user=user)
            
            # Return the token to the client
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            # Authentication failed
            return render(request, 'login.html', {'error': 'Invalid username or password'})

            # return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        # return render(request, 'login.html')
        # if user:
        #     if user.is_active:
        #         login(request, user) 
        #         token, _  = Token.objects.get_or_create(user=user)
        #         return Response({'token': token.key})
        #     else:
        #         return Response({'error': 'User account is not active.'}, status=status.HTTP_401_UNAUTHORIZED)
        # else:
        #     return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
       

class LogoutView(APIView):
    authentication_classes = (TokenAuthentication,)
    
    def post(self, request, format=None):
        
        logout(request)
        return Response({'msg' : 'logout successful'},status=status.HTTP_200_OK)
