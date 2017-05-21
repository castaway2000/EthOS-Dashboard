# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User
from models import Miners, Test, Miner_Info, Hosts
from rest_framework import viewsets
from serializers import UserSerializer, MinersSerializer, TestSerializer
import os


def get_miner_info():
    query = Miner_Info.objects.all().values()
    data = [query[0]['defunct'], query[0]['off'], query[0]['allowed'], query[0]['overheat'],
            query[0]['pool_info'], query[0]['pool'], query[0]['miner_version']]
    return data


def get_miner():
    query = Miners.objects.all().values()
    data = [query[0]['host'], query[0]['driver'], query[0]['selected_gpus'], query[0]['gpus'], query[0]['fanrpm'],
            query[0]['fanpercent'], query[0]['hash'], query[0]['miner'], query[0]['miner_hashes'],
            query[0]['hwerrors'], query[0]['gpu_models'], query[0]['bioses'], query[0]['default_core'],
            query[0]['default_mem'], query[0]['vramsize'], query[0]['core'], query[0]['mem'], query[0]['memstates'],
            query[0]['meminfo'], query[0]['voltage'], query[0]['overheatedgpu'], query[0]['throttled'],
            query[0]['powertune']]
    return data


def get_host_info():
    query = Hosts.objects.all().values()
    data = [query[0]['rx_kbps'], query[0]['tx_kbps'], query[0]['kernel'], query[0]['boot_mode'], query[0]['uptime'],
            query[0]['mac'], query[0]['hostname'], query[0]['rack_loc'], query[0]['ip'], query[0]['mobo'],
            query[0]['lan_chip'], query[0]['load'], query[0]['ram'], query[0]['cpu_temp'], query[0]['rofs'],
            query[0]['drive_name'], query[0]['freespace'], query[0]['temp'], query[0]['version'],
            query[0]['miner_secs'],
            query[0]['adl_error'], query[0]['proxy_problem'], query[0]['updating'], query[0]['connected_displays'],
            query[0]['resolution'],
            query[0]['gethelp'], query[0]['config_error'], query[0]['send_remote'], query[0]['autorebooted'],
            query[0]['status']]
    return data


def get_test_data():
    query = Test.objects.all().values()
    data = [query[0]['test_data'], query[0]['inputdata']]
    return data


def home(request):
    # context = get_gpuinfo()
    data = get_test_data()
    # hosts = get_host_info()
    # miner_info = get_miner_info()
    # miners = get_miner()
    # context = {'data': data, 'hosts': hosts, 'info': miner_info, 'miners': miners}
    context = {'data': data}
    return render(request, 'home/index.html', context)


def json_handler(hostname, json_data, hash_id):
    #TODO: new data per hostname vs overwriting each time.
    #TODO: insert new data and only get the latest info
    # Hosts.objects.update_or_create(request.GET)
    # Miners.objects.update_or_create(request.GET)
    # Miner_Info.objects.update_or_create(request.GET)
    return None


def api(request):
    # TODO: make this actually create a file so i can see whats being implemented
    hostname = None
    json_data = None
    hash_id = None
    data = "this url receives get requests for updating the gpu info to the dashboard"
    context = {'data': data}
    if request.GET:
        datakeys = request.GET.keys()
        for idx, key in enumerate(datakeys):
            # for testing purposes only
            # if key == 'test_data':
            #     Test.objects.update_or_create(request.GET)

            # for generating json files to test the final product with
            if idx == 0:
                hostname = request.GET[key]
                newfile = open(str('hostinfo.json'), str('w'))
                for line in hostname:
                    newfile.writelines(line)
                newfile.close()
            if idx == 1:
                json_data = request.GET[key]
                newfile = open(str('sendinfo.json'), str('w'))
                for line in json_data:
                    newfile.writelines(line)
                newfile.close()
            if idx == 2:
                hash_id = request.GET[key]
                newfile = open(str('hashinfo.json'), str('w'))
                for line in hash_id:
                    newfile.writelines(line)
                newfile.close()
        # json_handler(hostname, json_data, hash_id)
    return render(request, 'home/api.html', context)


class MinersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows miner data to be viewed or edited via gui.
    """
    queryset = Miners.objects.all()
    serializer_class = MinersSerializer


class TestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows test data to be viewed or edited via gui.
    """
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
