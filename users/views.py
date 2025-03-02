from django.shortcuts import render

# Create your views here.
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view
from twilio.rest import Client
import random

def index(request):
    return render(request, 'index.html')

def verify(request):
    return render(request, 'verify.html')

User = get_user_model()

TWILIO_ACCOUNT_SID = "your_twilio_account_sid"
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"
TWILIO_PHONE_NUMBER = "your_twilio_phone_number"

otp_store = {}  # Temporary storage for OTPs

@api_view(['POST'])
def send_otp(request):
    phone_number = request.data.get('phone_number')
    otp = str(random.randint(1000, 9999))
    otp_store[phone_number] = otp  # Store OTP temporarily

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    client.messages.create(
        body=f"Your OTP is {otp}",
        from_=TWILIO_PHONE_NUMBER,
        to=phone_number
    )
    return Response({"message": "OTP sent successfully!"})

@api_view(['POST'])
def verify_otp(request):
    phone_number = request.data.get('phone_number')
    otp = request.data.get('otp')

    if otp_store.get(phone_number) == otp:
        user, created = User.objects.get_or_create(phone_number=phone_number)
        user.is_verified = True
        user.save()
        return Response({"message": "Phone verified, account created!"})
    
    return Response({"error": "Invalid OTP"}, status=400)
