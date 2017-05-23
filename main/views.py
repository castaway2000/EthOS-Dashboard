# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User
from models import Test, Miner_Info
from rest_framework import viewsets
from serializers import UserSerializer, MinersSerializer, TestSerializer
import os


def get_host_info():
    query = Miner_Info.objects.all().values()
    print query
    # TODO: make dynamicly sized
    data = [
            query[0]['host'],
            # miner check info
            query[0]['defunct'], query[0]['off'], query[0]['allowed'], query[0]['overheat'],
            query[0]['pool_info'], query[0]['pool'], query[0]['miner_version'],
            
            # system related info
            query[0]['rx_kbps'], query[0]['tx_kbps'], query[0]['kernel'], query[0]['boot_mode'], query[0]['uptime'],
            query[0]['mac'], query[0]['hostname'], query[0]['rack_loc'], query[0]['ip'], query[0]['mobo'],
            query[0]['lan_chip'], query[0]['load'], query[0]['ram'], query[0]['cpu_temp'], query[0]['rofs'],
            query[0]['drive_name'], query[0]['freespace'], query[0]['temp'], query[0]['version'],
            query[0]['miner_secs'],
            query[0]['adl_error'], query[0]['proxy_problem'], query[0]['updating'], query[0]['connected_displays'],
            query[0]['resolution'],
            query[0]['gethelp'], query[0]['config_error'], query[0]['send_remote'], query[0]['autorebooted'],
            query[0]['status'],
            
            # GPU related info
            query[0]['driver'], query[0]['selected_gpus'], query[0]['gpus'], query[0]['fanrpm'],
            query[0]['fanpercent'], query[0]['hash'], query[0]['miner'], query[0]['miner_hashes'],
            query[0]['hwerrors'], query[0]['gpumodels'], query[0]['bioses'], query[0]['default_core'],
            query[0]['default_mem'], query[0]['vramsize'], query[0]['core'], query[0]['mem'], query[0]['memstates'],
            query[0]['meminfo'], query[0]['voltage'], query[0]['overheatedgpu'], query[0]['throttled'],
            query[0]['powertune']
            ]
    return data


def get_test_data():
    query = Test.objects.all().values()
    data = [query[0]['test_data'], query[0]['inputdata']]
    return data


def home(request):
    hosts = get_host_info()
    context = {'hosts': hosts}
    # TODO: make pretty
    return render(request, 'home/index.html', context)


def json_handler(hostname, json_data):
    #TODO: write logic to add the hostname into the the json data 
    #TODO: 
    json_data['host'] = hostname
    
    # json_data = {
    # "defunct": 0,
    # "off": "0",
    # "allowed": 1,
    # "overheat": 0,
    # "pool_info": "stratumproxy enabled\nproxywallet 0x8C866Cf8a4878032e172D72d6136d114de3beCeA\nproxypool1 us2.ethermine.org:4444\nproxypool2 us1.ethermine.org:4444",
    # "pool": "us2.ethermine.org:4444",
    # "miner_version": "v9.3",
    # "rx_kbps": "0.80",
    # "tx_kbps": "0.71",
    # "kernel": "4.8.17-ethos38",
    # "boot_mode": "uefi",
    # "uptime": "1566",
    # "mac": "1c1b0d689143",
    # "hostname": "689143",
    # "rack_loc": "",
    # "ip": "192.168.1.45",
    # "mobo": "990FXA-UD3 R5",
    # "lan_chip": "Realtek Semiconductor Co., Ltd. RTL8111\/8168\/8411 PCI Express Gigabit Ethernet Controller (rev 0c)",
    # "load": "0.30",
    # "ram": "4",
    # "cpu_temp": "52",
    # "cpu_name": "AMD Sempron(tm) 140 Processor",
    # "rofs": 38,
    # "drive_name": "Ultra USB 3.0 4C530001230227102412",
    # "freespace": 3.7,
    # "temp": "52.00 49.00 49.00 50.00 51.00 50.00",
    # "version": "1.2.1",
    # "miner_secs": 1507,
    # "adl_error": "",
    # "proxy_problem": "working",
    # "updating": "0",
    # "connected_displays": "",
    # "resolution": "",
    # "gethelp": "",
    # "config_error": "",
    # "send_remote": "http:\/\/stealthyhosting.com\/bpool.txt",
    # "autorebooted": "0",
    # "status": "173.5 hash: miner active",
    # "driver": "amdgpu",
    # "selected_gpus": "",
    # "gpus": "6",
    # "fanrpm": "4182 4182 4182 4182 4182 4182",
    # "fanpercent": "93 93 93 93 93 93",
    # "hash": "174.14",
    # "miner": "claymore",
    # "miner_hashes": "29.12 29.12 29.52 29.44 29.33 27.61",
    # "gpumodels": "01 Ellesmere RX 480 113-2E3470U.S52 Samsung\n02 Ellesmere RX 480 113-2E3470U.S52 Samsung\n05 Ellesmere RX 480 113-2E3470U.S52 Samsung\n06 Ellesmere RX 480 113-2E3470U.S52 Samsung\n09 Ellesmere RX 480 113-2E3470U.S52 Samsung\n0a Ellesmere RX 480 113-2E3470U.S52 Samsung",
    # "bioses": "113-2E3470U.S52 113-2E3470U.S52 113-2E3470U.S52 113-2E3470U.S52 113-2E3470U.S52 113-2E3470U.S52",
    # "default_core": "1150 1150 1150 1150 1150 1150",
    # "default_mem": "2150 2150 2150 2150 2150 2150",
    # "vramsize": "8 8 8 8 8 8",
    # "core": "1150 1150 1150 1150 1150 1150",
    # "mem": "2160 2160 2200 2190 2180 2160",
    # "memstates": "1 1 1 1 1 1",
    # "meminfo": "GPU0:01.00.0:Radeon RX 480:113-2E3470U.S52:Samsung K4G80325FB\nGPU1:02.00.0:Radeon RX 480:113-2E3470U.S52:Samsung K4G80325FB\nGPU2:05.00.0:Radeon RX 480:113-2E3470U.S52:Samsung K4G80325FB\nGPU3:06.00.0:Radeon RX 480:113-2E3470U.S52:Samsung K4G80325FB\nGPU4:09.00.0:Radeon RX 480:113-2E3470U.S52:Samsung K4G80325FB\nGPU5:0a.00.0:Radeon RX 480:113-2E3470U.S52:Samsung K4G80325FB",
    # "voltage": "0.00 0.00 0.00 0.00 0.00 0.00",
    # "overheatedgpu": "",
    # "throttled": "",
    # "powertune": "5 5 5 5 5 5"
    # }
    
    Miner_Info.objects.update_or_create(json_data)
    return None


def api(request):
    # TODO: make this actually create a file so i can see whats being implemented
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
        
        # for generating json files to test the final product with
        if request.GET['hostname']:
            hostname = request.GET['hostname']
        if request.GET['url_style']:
            json_data = request.GET['url_style']
        if request.GET['hash']:
            hash_id = request.GET['hash']
        json_handler(hostname, json_data)
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
