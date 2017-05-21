from django.contrib.auth.models import User
from models import Miners, Test
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class TestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Test
        fields = ('test_data', 'inputdata')


class MinersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Miners
        fields = ('driver', 'selected_gpus', 'gpus', 'fanrpm', 'fanpercent', 'hash', 'miner', 'miner_hashes',
                  'hwerrors', 'gpu_models', 'bioses', 'default_core', 'default_mem', 'vramsize', 'core', 'mem',
                  'memstates', 'meminfo', 'voltage', 'overheatedgpu', 'throttled', 'powertune')
