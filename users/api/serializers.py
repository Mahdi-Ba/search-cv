from ..models import User
from  rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField('get_fullname')
    password = serializers.CharField(write_only=True, required=False)
    first_name = serializers.CharField(max_length=200, required=False)
    last_name = serializers.CharField(max_length=200, required=False)
    national_code = serializers.CharField(max_length=200, required=False)
    birth_date = serializers.DateField(required=False)
    mobile = serializers.CharField(read_only=False, required=False)
    file = serializers.FileField(required=False)
    # attrs = serializers.JSONField(required=False)

    
    class Meta:
        model = User
        fields = ['mobile', 'first_name', 'last_name', 'full_name', 'national_code', 'password', 'birth_date','file','attrs']
        # fields = '__all__'

    def get_fullname(self, instance):
        return instance.first_name + ' ' + instance.last_name

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name) if validated_data.get('first_name') is not None else instance.first_name
        instance.last_name = validated_data.get('last_name', instance.last_name) if validated_data.get('last_name') is not None else instance.last_name
        instance.national_code = validated_data.get('national_code', instance.national_code) if validated_data.get('national_code') is not None else instance.national_code
        instance.birth_date = validated_data.get('birth_date', instance.birth_date) if validated_data.get('birth_date') is not None else instance.birth_date
        instance.file = validated_data.get('file', instance.file) if validated_data.get('file') is not None else instance.file
        # instance.attrs = validated_data.get('attrs', instance.attrs)
        instance.save()
        return instance
