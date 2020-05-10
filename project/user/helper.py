from rest_framework.authtoken.models import Token
from .models import UserModel
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
import io

def message(text: str):

    return {
        "message": text
    }

def get_data(request):
    # convert json data to dictionary
    data = io.BytesIO(request.body)
    data = JSONParser().parse(data)

    return data

class AuthenticateResult():
    def __init__(self, user, token):
        self.user = user
        self.token = token

def handle_login(request, response):
    

    if not 'token' in request.COOKIES:

        return response(
            message("login required"),
            status = status.HTTP_405_METHOD_NOT_ALLOWED
        )

    
    try:
        # find user that token belongs to.
        token_key = request.COOKIES['token']
        token = Token.objects.get(key = token_key)
        
        return token.user

    except:
        return response(
            message('something wrong with user token.'),
            status = status.HTTP_500_INTERNAL_SERVER_ERROR
        )

login_is_ok = lambda login_status: isinstance(login_status, UserModel)

def login_required(func):

    def decorator(request):

        user_status = handle_login( request, Response )

        if not login_is_ok( user_status ):
            return user_status
    
        return func(request, user_status)

    return decorator

    
