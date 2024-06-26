from django.shortcuts import render
from django.http import JsonResponse
from .models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password , make_password
import json
from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404



@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if password != confirm_password:
            return JsonResponse({'error': 'Passwords do not match'}, status=400)

        if User.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Email already exists'}, status=400)

        user = User.objects.create(name=name, email=email, password=make_password(password))
        user.save()
        return JsonResponse({'message': 'User registered successfully'}, status=201)
    
    return HttpResponseBadRequest('Invalid request method')

@csrf_exempt
def get_register(request, user_id):
    if request.method == "GET":
        try:
            user = get_object_or_404(User, id=user_id)
            user_data={
                'id': user.id,
                "name": user.name,
                'email': user.email
            }
            return JsonResponse(user_data , status = 200)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
    
    return HttpResponseBadRequest('Invalid request method')
        

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')

        try:
            user = User.objects.get(email=email)
            if check_password(password, user.password):
                return JsonResponse({'message': 'Login successful'}, status=200)
            else:
                return JsonResponse({'error': 'Invalid credentials'}, status=400)
        except User.DoesNotExist:
            return JsonResponse({'error': 'Invalid credentials'}, status=400)