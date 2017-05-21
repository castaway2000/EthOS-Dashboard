# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
#TODO: create a hostname associateion for all the data.

class Test(models.Model):
    test_data = models.CharField(max_length=256, blank=True, null=True, default=None)
    inputdata = models.CharField(max_length=256, blank=True, null=True, default=None)


class Hosts(models.Model):
    objects = models.Manager
    rx_kbps = models.CharField(max_length=256, blank=True, null=True, default=None)
    tx_kbps = models.CharField(max_length=256, blank=True, null=True, default=None)
    kernel = models.CharField(max_length=256, blank=True, null=True, default=None)
    boot_mode = models.CharField(max_length=256, blank=True, null=True, default=None)
    uptime = models.CharField(max_length=256, blank=True, null=True, default=None)
    mac = models.CharField(max_length=256, blank=True, null=True, default=None)
    hostname = models.CharField(max_length=256, blank=True, null=True, default=None)
    rack_loc = models.CharField(max_length=256, blank=True, null=True, default=None)
    ip = models.CharField(max_length=256, blank=True, null=True, default=None)
    mobo = models.CharField(max_length=256, blank=True, null=True, default=None)
    lan_chip = models.CharField(max_length=256, blank=True, null=True, default=None)
    load = models.CharField(max_length=256, blank=True, null=True, default=None)
    ram = models.CharField(max_length=256, blank=True, null=True, default=None)
    cpu_temp = models.CharField(max_length=256, blank=True, null=True, default=None)
    rofs = models.CharField(max_length=256, blank=True, null=True, default=None)
    drive_name = models.CharField(max_length=256, blank=True, null=True, default=None)
    freespace = models.CharField(max_length=256, blank=True, null=True, default=None)
    temp = models.CharField(max_length=256, blank=True, null=True, default=None)
    version = models.CharField(max_length=256, blank=True, null=True, default=None)
    miner_secs = models.CharField(max_length=256, blank=True, null=True, default=None)
    adl_error = models.CharField(max_length=256, blank=True, null=True, default=None)
    proxy_problem = models.CharField(max_length=256, blank=True, null=True, default=None)
    updating = models.CharField(max_length=256, blank=True, null=True, default=None)
    connected_displays = models.CharField(max_length=256, blank=True, null=True, default=None)
    resolution = models.CharField(max_length=256, blank=True, null=True, default=None)
    gethelp = models.CharField(max_length=256, blank=True, null=True, default=None)
    config_error = models.CharField(max_length=256, blank=True, null=True, default=None)
    send_remote = models.CharField(max_length=256, blank=True, null=True, default=None)
    autorebooted = models.CharField(max_length=256, blank=True, null=True, default=None)
    status = models.CharField(max_length=256, blank=True, null=True, default=None)


class Miners(models.Model):
    objects = models.Manager
    host = models.ForeignKey(Hosts)
    driver = models.CharField(max_length=256, blank=True, null=True, default=None)
    selected_gpus = models.CharField(max_length=256, blank=True, null=True, default=None)
    gpus = models.CharField(max_length=256, blank=True, null=True, default=None)
    fanrpm = models.CharField(max_length=256, blank=True, null=True, default=None)
    fanpercent = models.CharField(max_length=256, blank=True, null=True, default=None)
    hash = models.CharField(max_length=256, blank=True, null=True, default=None)
    miner = models.CharField(max_length=256, blank=True, null=True, default=None)
    miner_hashes = models.CharField(max_length=256, blank=True, null=True, default=None)
    hwerrors = models.CharField(max_length=256, blank=True, null=True, default=None)
    gpu_models = models.CharField(max_length=256, blank=True, null=True, default=None)
    bioses = models.CharField(max_length=256, blank=True, null=True, default=None)
    default_core = models.CharField(max_length=256, blank=True, null=True, default=None)
    default_mem = models.CharField(max_length=256, blank=True, null=True, default=None)
    vramsize = models.CharField(max_length=256, blank=True, null=True, default=None)
    core = models.CharField(max_length=256, blank=True, null=True, default=None)
    mem = models.CharField(max_length=256, blank=True, null=True, default=None)
    memstates = models.CharField(max_length=256, blank=True, null=True, default=None)
    meminfo = models.CharField(max_length=256, blank=True, null=True, default=None)
    voltage = models.CharField(max_length=256, blank=True, null=True, default=None)
    overheatedgpu = models.CharField(max_length=256, blank=True, null=True, default=None)
    throttled = models.CharField(max_length=256, blank=True, null=True, default=None)
    powertune = models.CharField(max_length=256, blank=True, null=True, default=None)


class Miner_Info(models.Model):
    objects = models.Manager
    gpu = models.ForeignKey(Miners)
    defunct = models.CharField(max_length=256, blank=True, null=True, default=None)
    off = models.CharField(max_length=256, blank=True, null=True, default=None)
    allowed = models.CharField(max_length=256, blank=True, null=True, default=None)
    overheat = models.CharField(max_length=256, blank=True, null=True, default=None)
    pool_info = models.CharField(max_length=256, blank=True, null=True, default=None)
    pool = models.CharField(max_length=256, blank=True, null=True, default=None)
    miner_version = models.CharField(max_length=256, blank=True, null=True, default=None)