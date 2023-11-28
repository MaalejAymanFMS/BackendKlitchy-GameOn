from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from user.models import User

def index(request):
    return HttpResponse("Hello, world. You're at the user index.")


def get_user_by_pin(request, pin):
    try:
        # Assuming you have a model with a field named 'pin' to store the user's PIN.
        # Replace 'YourModel' with the actual name of your model.
        user = User.objects.get(pin=pin)  # Assuming 'profile' is a related model.
        
        # You can add additional checks here if needed (e.g., check if the PIN is valid).
        
        # Serialize the user data to JSON.
        user_data = {
            'password': user.password,
            'email': user.email,
            'token':user.token,
            'role':user.role
            # Add more fields as needed.
        }
        
        # Return the user data as JSON response.
        return JsonResponse(user_data)
    except User.DoesNotExist:
        # Return a JSON response indicating that the user with the given PIN was not found.
        error_response = {'error': 'User not found'}
        return JsonResponse(error_response, status=404)

