import re
import json
import bcrypt, jwt

from django.http  import JsonResponse
from django.views import View
from django.conf  import settings

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


class LoginView(View):
    def post(self,request):
        data = json.loads(request.body)

        try:
            email    = data['email']
            password = data['password']
            user     = User.objects.get(email=email)
            # print(email)
            # print(password)
            print(user.name)
            print(user.password)

            print(bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')))

            if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse({'message': 'INVALID_PW'}, status=401)

            access_token = jwt.encode({'user_id': user.id}, settings.SECRET_KEY, 'HS256')

            return JsonResponse({
                'message'     : 'SUCCESS',
                'access_token': access_token
                }, status=200)

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
        except User.DoesNotExist:
            return JsonResponse({'message': 'INVALID_USER'}, status=401)