from rest_framework import serializers

from django.contrib.auth.models import User

class RegistrationSerializer(serializers.ModelSerializer):

    User._meta.get_field('email')._unique = True

    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'password', 'confirm_password']
        extra_kwargs = {
            'password':{'write_only': True}
        }

    def save(self):
        account = User(email=self.validated_data['email'],
                       username = self.validated_data['username'],
                       first_name = self.validated_data['first_name'],
                       last_name = self.validated_data['last_name']
            )
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']

        if password != confirm_password:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        account.set_password(password)
        account.save()
        return account
