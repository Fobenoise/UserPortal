from django.shortcuts import render

# Create your views here.
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserProfileSerializer
from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile, RoleProfile
from django.views.decorators.http import require_POST


def index_view(requests):
    return render(requests, 'myapp/index.html')



@api_view(['POST'])
def user_list(request):
    # Handle GET request (retrieve users)
    # if request.method == 'GET':
    #     return
        #users = UserProfile.objects.all()
        #serializer = UserProfileSerializer(users, many=True)
        #return Response(serializer.data)

    # Handle POST request (add a new user)
    # elif request.method == 'POST':
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def user_table_view(request):
    users = UserProfile.objects.all()  # Fetch all users from the database
    roles = RoleProfile.objects.all()  # Fetch all roles from the database
    context = {
        'users': users,
        'roles': roles,
    }
    return render(request, 'myapp/user_list.html', context)


def user_edit_view(request):
    if request.method == 'POST':
        # Handle updating or adding a user
        user_id = request.POST.get('user_id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        role_id = request.POST.get('role')  # Get the selected role from the form

        if user_id:  # If there's a user_id, we are updating an existing user
            user = get_object_or_404(UserProfile, id=user_id)
            user.name = name
            user.email = email
            if role_id:
                user.role = RoleProfile.objects.get(id=role_id)  # Assign role if selected
            user.save(), role.save()
        else:  # No user_id means we are creating a new user
            if name and email:
                role = RoleProfile.objects.get(id=role_id) if role_id else None
                UserProfile.objects.create(name=name, email=email, role=role)
                
                
        return redirect('user-edit')  # Redirect to the same page after adding/updating

    # Fetch all users and available roles
    users = UserProfile.objects.all()
    roles = RoleProfile.objects.all()
    
    return render(request, 'myapp/user_edit.html',  {'users': users, 'roles': roles})




@require_POST
def delete_user_view(request, user_id):
    user = get_object_or_404(UserProfile, id=user_id)
    user.delete()
    return redirect('user-edit')


@require_POST
def update_user_view(request, user_id):
    user = get_object_or_404(UserProfile, id=user_id)
    
    user.name = request.POST.get('name')
    user.email = request.POST.get('email')
    
    role_id = request.POST.get('role')
    
    if role_id:
        # Fetch the RoleProfile object and assign it to the user
        user.role = get_object_or_404(RoleProfile, id=role_id)
    else:
        # If no role is selected, set the role to None
        user.role = None
    
    user.save()
    
    return redirect('user-edit')

@require_POST
def delete_user_view(request, user_id):
    user = get_object_or_404(UserProfile, id=user_id)
    user.delete()
    return redirect('user-edit')

def user_roles(request):
    roles = RoleProfile.objects.all()  # Fetch all users from the database
    return render(request, 'myapp/roles_list.html', {'roles': roles})
    # return render(request, 'myapp/roles_list.html', {'roles': myroles})

def role_edit_view(request):
    if request.method == 'POST':
        # Add a new user
        name = request.POST.get('name')
        if name:
            RoleProfile.objects.create(name=name)
            return redirect('role-edit')  # Redirect to the same page after adding

    roles = RoleProfile.objects.all()
    return render(request, 'myapp/role_edit.html', {'roles': roles})

@require_POST
def update_role_view(request, role_id):
    role = get_object_or_404(RoleProfile, id=role_id)
    role.name = request.POST.get('name')
    role.save()
    return redirect('role-edit')

@require_POST
def delete_role_view(request, role_id):
    role = get_object_or_404(RoleProfile, id=role_id)
    role.delete()
    return redirect('role-edit')