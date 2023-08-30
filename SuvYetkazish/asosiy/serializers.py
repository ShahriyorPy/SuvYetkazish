from django.core.exceptions import ValidationError
from rest_framework  import serializers
from .models import *

class SuvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suv
        fields = "__all__"

    def validate_litr(self, qiymat):
        if qiymat > 19:
            raise ValidationError("Bunday katta litrlarda suv sotilmaydi")
        return qiymat

class MijozSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mijoz
        fields = "__all__"

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = "__all__"

    def validate_yosh(self, qiymat):
        if qiymat < 19:
            raise ValidationError("Yoshingiz mos kelmaydi")
        return qiymat

class HaydovchiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Haydovchi
        fields = "__all__"

class BuyurtmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyurtma
        fields = "__all__"

    def validate_mijoz(self, qiymat):
        if qiymat.qarz > 50000:
            raise ValidationError("Qarzingiz juda ko’p, buyurtma qilolmaysiz!")
        return qiymat