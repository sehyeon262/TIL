from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers


class CustomRegisterSerializer(RegisterSerializer):
    age = serializers.IntegerField()

    def get_cleaned_data(self):
        data = super().get_cleaned_data()  # 유저, 이메일, 패스워드 들어있음
        data['age'] = self.validated_data.get('age')  # age 추가
        return data
    
    def save(self, request):
        user = super().save(request)
        user.age = self.validated_data.get('age')
        user.save()
        return user