from rest_framework import serializers
from .models import Account


class AccountCreateSerializer(serializers.Serializer):
    phone_number = serializers.CharField(required=True)
    passport_number = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    martial_status = serializers.CharField(required=True)
    date_of_birth = serializers.DateField(required=True)
    visa_type = serializers.CharField(required=True)

    def validate(self, data):
        # Check for duplicate email and passport number
        email = data.get("email")
        passport_number = data.get("passport_number")

        if email and Account.objects.filter(email=email).exists():
            raise serializers.ValidationError("Email already exists.")

        if (
            passport_number
            and Account.objects.filter(passport_number=passport_number).exists()
        ):
            raise serializers.ValidationError("Passport number already exists.")

        return data


class AccountListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"


class AccountUpdateSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(required=True)
    passport_number = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    martial_status = serializers.CharField(required=True)
    date_of_birth = serializers.DateField(required=True)
    visa_type = serializers.CharField(required=True)

    class Meta:
        model = Account  # Make sure to use the correct model class here
        exclude = ['user']  # Exclude the 'user' field from the serializer
