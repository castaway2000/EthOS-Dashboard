# EthOS-Dashboard
this is an open source reverse engineered personal dashboard for the EthOS etherium mining operating system

#### news:
11/19/2018 this is no longer supported by me directly. I welcome contributions from the community and all those who have forks to update the dashboard and add any functionality they you fit. 

## To use:
### configure
run pip install -r requirements.txt

### then
simply update the php file $url and $hook to your own and make sure to point your GET requests to the www.website.com/API


### run
python manage.py runserver ip:port

and then make sure your django ip address and port point to a hostname


### after
place the php script in the respective spot and wait for the cron to run against the dashboard and get your stats.



## About the app:
### /minerstat
houses all the settings and core url routings

### /main
houses all the views, models and serializers for the graphical api

### /templates
houses all the html django templates for the data to be displayed. 

### send.php
I built this for a friend as a fun project so this file was provided to me by him. This file is critical specifically to get all the details from the GPU and mining processes that EthOS has provided. 

As I understand this file lives on the server and is built into EthOS you would simply replace your default send.php file with this one. I wrote in the docs that it lives as a cronjob so you would find or make the php file and then make a cronjob to act as your polling service

to find it you should run:
file / -name send.php

to set a new cron:
crontab -e

The php script is polling for data from the GPU. Each time the script is called it polls the data and sends a snapshot of it to the backend via the dashboard url paramiters. It is then stored and can be served upon the basic dashboard I made when you load the website. 



