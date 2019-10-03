from rest_framework import serializers

from account.models import CustomUser



class RegistrationSerialzer (serializers.ModelSerializer):
    password2 = serializers.CharField(style = {'input_type' : 'password'}, write_only = True)
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'address', 'password', 'password2']
        extra_kwargs = {
            'password' : {'write_only' : True}
        }

    def save(self):
        user = CustomUser(
            username = self.validated_data['username'],
            email = self.validated_data['email'],
            address = self.validated_data['address']
        )
        
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        if password != password2 :
            raise serializers.ValidationError ({'password' : 'Password must match'})
        
        user.set_password(password)
        user.save()
        return user