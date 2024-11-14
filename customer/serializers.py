from rest_framework import serializers
from .models import Customer
import math

class RegistrationSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    monthly_income = serializers.IntegerField()
    phone_number = serializers.CharField(max_length=15)

    def validate_age(self, value):
        if value < 0:
            raise serializers.ValidationError("Age must be postive.")
        if value > 100:
            raise serializers.ValidationError("Age must be less than or equal to 100.")
        return value

    def validate_monthly_income(self, value):
        if value < 0:
            raise serializers.ValidationError("Monthly income cannot be negative.")
        return value

class CustomerResponseSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    customer_id = serializers.IntegerField(source="id")
    
    class Meta:
        model = Customer
        fields = ('customer_id', 'name', 'age', 'monthly_salary', 'approved_limit', 'phone_number')

    def get_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
