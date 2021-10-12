import json
import re
import bcrypt, jwt

from django.http import JsonResponse
from django.views import View
from django.conf.global_settings import SECRET_KEY

from user.models import User

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