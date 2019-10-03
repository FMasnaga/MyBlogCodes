from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import RegistrationSerialzer

@api_view(['POST'])
def registration_view (request):
    if request.method == 'POST':
        serializer = RegistrationSerialzer(data = request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['message'] = 'Successfully register'
            data['email'] = user.email
            data['username'] = user.username
            data['address'] = user.address
            
        else :
            data = serializer.errors
        
        return Response(data)
    
        
    
