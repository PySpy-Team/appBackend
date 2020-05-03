from rest_framework.parsers import JSONParser
import io

def get_data(request):
    # convert json data to dictionary
    data = io.BytesIO(request.body)
    data = JSONParser().parse(data)

    return data

class AuthenticateResult():
    def __init__(self, user, token):
        self.user = user
        self.token = token