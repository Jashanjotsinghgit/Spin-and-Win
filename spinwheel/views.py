from django.shortcuts import render
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model
import random

def spin(request):
    return render(request, 'spin.html')

User = get_user_model()

@api_view(['POST'])
def spin_wheel(request):
    user_id = request.data.get('user_id')
    user = User.objects.get(id=user_id)

    if user.has_spun:
        return Response({"error": "You have already spun the wheel!"}, status=400)

    prizes = ["Nothing", "Gift Card", "Discount", "Free Product"]
    result = random.choice(prizes)

    user.has_spun = True  # Update status
    user.save()
    
    return Response({"message": f"You won: {result}!"})
