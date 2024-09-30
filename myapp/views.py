from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserProfileSerializer
from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile
from django.views.decorators.http import require_POST


def index_view(requests):
    return render(requests, 'myapp/index.html')


@api_view(['GET', 'POST'])
def user_list(request):
    # Handle GET request (retrieve users)
    if request.method == 'GET':
        users = UserProfile.objects.all()
        serializer = UserProfileSerializer(users, many=True)
        return Response(serializer.data)

    # Handle POST request (add a new user)
    elif request.method == 'POST':
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def user_table_view(request):
    users = UserProfile.objects.all()  # Fetch all users from the database
    return render(request, 'myapp/user_list.html', {'users': users})


def user_edit_view(request):
    if request.method == 'POST':
        # Add a new user
        name = request.POST.get('name')
        email = request.POST.get('email')
        if name and email:
            UserProfile.objects.create(name=name, email=email)
            return redirect('user-edit')  # Redirect to the same page after adding

    users = UserProfile.objects.all()
    return render(request, 'myapp/user_edit.html', {'users': users})

@require_POST
def delete_user_view(request, user_id):
    user = get_object_or_404(UserProfile, id=user_id)
    user.delete()
    return redirect('user-edit')


def user_edit_view(request):
    if request.method == 'POST' and 'name' in request.POST and 'email' in request.POST:
        # Add a new user
        name = request.POST.get('name')
        email = request.POST.get('email')
        if name and email:
            UserProfile.objects.create(name=name, email=email)
            return redirect('user-edit')  # Redirect to the same page after adding

    users = UserProfile.objects.all()
    return render(request, 'myapp/user_edit.html', {'users': users})

@require_POST
def update_user_view(request, user_id):
    user = get_object_or_404(UserProfile, id=user_id)
    user.name = request.POST.get('name')
    user.email = request.POST.get('email')
    user.save()
    return redirect('user-edit')

@require_POST
def delete_user_view(request, user_id):
    user = get_object_or_404(UserProfile, id=user_id)
    user.delete()
    return redirect('user-edit')