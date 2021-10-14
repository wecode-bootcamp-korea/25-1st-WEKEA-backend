import json
import re
import bcrypt
import jwt

from django.http  import JsonResponse
from django.db    import transaction
from django.views import View
from django.conf.global_settings import SECRET_KEY

from user.models import User, Address

class SignUp(View):
    @transaction.atomic
    def post(self, request):
        data              = json.loads(request.body)
        REGX_EMAIL        = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        REGX_PASSWORD     = '^(?=.*\d)(?=.*[a-zA-Z])[0-9a-zA-Z!@#$%^&*]{8,20}$'
        REGX_BIRTHDAY     = "^([12]\\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\\d|3[01]))$"
        REGX_MOBILE_PHONE = '\d{10,11}$'
        REGX_ZIP_CODE     = '\d{5}$'

        try:
            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({'message': 'EXIST_EMAIL'}, status=400)

            if not re.match(REGX_EMAIL, data['email']):
                return JsonResponse({'message': 'INVALID_EMAIL_FORM'}, status=400)

            if not re.match(REGX_PASSWORD, data['password']):
                return JsonResponse({'message': 'INVALID_PASSWORD_FORM'}, status=400)

            if not re.match(REGX_MOBILE_PHONE, data['mobile_phone']):
                return JsonResponse({'message': 'INVALID_MOBILE_PHONE_FORM'}, status=400)

            if not re.match(REGX_BIRTHDAY, data['birthday']):
                return JsonResponse({'message': 'INVALID_BIRTHDAY_FORM'}, status=400)

            if not re.match(REGX_ZIP_CODE, data['zip_code']):
                return JsonResponse({'message': 'INVALID_ZIP_CODE_FORM'}, status=400)

            password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            
            create_user = User(
                last_name      = data['last_name'],
                first_name     = data['first_name'],
                gender         = data['gender'],
                email          = data['email'],
                password       = password,
                mobile_phone   = data['mobile_phone'],
                favorite_store = data['favorite_store'],
                birthday       = data['birthday']
            )
            
            create_user.save()

            create_adderss = Address(
                user_id         = create_user.id,
                name_of_street  = data['name_of_street'],
                detail_address  = data['detail_address'],
                zip_code        = data['zip_code'],
                default_address = data['default_address'],
            )
            
            create_adderss.save()

            return JsonResponse({'message': 'SUCCESS'}, status=201)
        
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

class LoginView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            user = User.objects.get(email = data['email'])

            if not (user and bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8'))):
                return JsonResponse({"message" : "INVALID_USER"}, status = 401)

        except KeyError:
            return JsonResponse({"message" : "KeyError"}, status = 400)

        encoded_jwt = jwt.encode({'user' : user.id}, SECRET_KEY, algorithm = 'HS256')

        return JsonResponse({'access_token' : encoded_jwt}, status = 201)
