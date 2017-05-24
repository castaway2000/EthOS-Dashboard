# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User
from models import Test, Miner_Info
from rest_framework import viewsets
from serializers import UserSerializer, MinersSerializer, TestSerializer
from tables import MinerTable
import os, ast


def get_host_info():
    query = Miner_Info.objects.all().values()
    miners = []
    for data in query:
        info = [
                data['host'],
                # miner check info
                data['defunct'], data['off'], data['allowed'], data['overheat'],
                data['pool_info'], data['pool'], data['miner_version'],
                
                # system related info
                data['rx_kbps'], data['tx_kbps'], data['kernel'], data['boot_mode'], data['uptime'],
                data['mac'], data['hostname'], data['rack_loc'], data['ip'], data['mobo'],
                data['lan_chip'], data['load'], data['ram'], data['cpu_temp'], data['rofs'],
                data['drive_name'], data['freespace'], data['temp'], data['version'],
                data['miner_secs'],
                data['adl_error'], data['proxy_problem'], data['updating'], data['connected_displays'],
                data['resolution'],
                data['gethelp'], data['config_error'], data['send_remote'], data['autorebooted'],
                data['status'],
                
                # GPU related info
                data['driver'], data['selected_gpus'], data['gpus'], data['fanrpm'],
                data['fanpercent'], data['hash'], data['miner'], data['miner_hashes'],
                data['hwerrors'], data['gpumodels'], data['bioses'], data['default_core'],
                data['default_mem'], data['vramsize'], data['core'], data['mem'], data['memstates'],
                data['meminfo'], data['voltage'], data['overheatedgpu'], data['throttled'],
                data['powertune']
                ]
        miners.append(info)
    return miners


def get_test_data():
    query = Test.objects.all().values()
    data = [data['test_data'], data['inputdata']]
    return data


def home(request):
    # hosts = get_host_info()
    # context = {'hosts': hosts}
    # TODO: make pretty
    tables = MinerTable(Miner_Info.objects.all())
    context = { 'tables': tables }
    return render(request, 'home/index.html', context)


def api(request):
    hostname = None
    json_data = None
    hash_id = None
    data = "this url receives get requests for updating the gpu info to the dashboard"
    context = {'data': data}
    if request.GET:
        # for testing purposes only
        # if request.GET['test_data']:
        #     Test.objects.update_or_create(request.GET)
        # break
        if request.GET['hash']:
            hash_id = request.GET['hash']
        if request.GET['url_style']:
            json_data = ast.literal_eval(request.GET['url_style'])
            if request.GET['hostname']:
                hostname = request.GET['hostname']
                json_data['host'] = hostname
        Miner_Info.objects.filter(host=json_data['host']).update_or_create(json_data)
    return render(request, 'home/api.html', context)


class MinersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows miner data to be viewed or edited via gui.
    """
    queryset = Miner_Info.objects.all()
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
