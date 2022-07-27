from rest_framework import serializers
from .models import Supers

class SupersSerializer(serializers.ModelSerializer):
    super_type_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Supers
        fields = ['id', 'name', 'alter_ego', 'primary_ability', 'secondary_ability', 'catchphrase', 'super_type', 'super_type_id']
        depth = 1

        