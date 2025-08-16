from rest_framework import serializers
from signals.models import Signals


class SignalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signals
        fields = "__all__"
