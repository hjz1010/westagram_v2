import re
import json
import bcrypt

from django.http import JsonResponse
from django.views import View

from .models import User

REGEX_EMAIL    = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
REGEX_PASSWORD = '^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{4,}$'

class SignupView(View):
    def post(self,request):
        data = json.loads(request.body)
        try:
            email        = data['email']
            name         = data['name']
            password     = data['password']
            phone_number = data['phone_number']
            
            global REGEX_EMAIL
            global REGEX_PASSWORD

            if not re.match(REGEX_EMAIL, email):
                return JsonResponse({'message': 'INVALID_EMAIL'}, status=400)
            if not re.match(REGEX_PASSWORD, password):
                return JsonResponse({'message': 'INVALID_PASSWORD'}, status=400)
            
            if User.objects.filter(email = email):
                return JsonResponse({'message': 'EMAIL_DUPLICATION'}, status=400)

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            User.objects.create(
                email        = email,
                name         = name,
                password     = hashed_password,
                phone_number = phone_number
            )
            return JsonResponse({'message': 'SUCCESS'}, status=201)

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
