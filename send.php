git stafunction get_stats()
{
        $gpus = trim(file_get_contents("/var/run/ethos/gpucount.file"));
        $driver = trim(`/opt/ethos/sbin/ethos-readconf driver`);
        $miner = trim(`/opt/ethos/sbin/ethos-readconf miner`);
        list($rx_kbps,$tx_kbps) = sample_kbps();

        // miner check info
        $send['defunct'] = intval(trim(file_get_contents("/var/run/ethos/defunct.file")));
        $send['off'] = trim(`/opt/ethos/sbin/ethos-readconf off`);
        $send['allowed'] = intval(trim(file_get_contents("/opt/ethos/etc/allow.file")));
        $send['overheat'] = intval(trim(file_get_contents("/var/run/ethos/overheat.file")));
        $send['pool_info'] = trim(`cat /home/ethos/local.conf | grep -v '^#' | egrep -i 'pool|wallet|proxy'`);
        $send['pool'] = trim(`/opt/ethos/sbin/ethos-readconf proxypool1`);
        $send['miner_version'] = trim(`cat /var/run/ethos/miner.versions | grep '$miner ' | cut -d" " -f2 | head -1`);






        // system related info

        $send['rx_kbps'] = $rx_kbps;
        $send['tx_kbps'] = $tx_kbps;
        $send['kernel'] = trim(`/bin/uname -r`);
        $send['boot_mode'] = trim(`/opt/ethos/sbin/ethos-readdata bootmode`);
        $send['uptime'] = trim(`cat /proc/uptime | cut -d"." -f1`);
        $send['mac'] = trim(`/sbin/ifconfig | grep HW | awk '{print \$NF}' | sed 's/://g'`);
        $send['hostname'] = trim(`/sbin/ifconfig | grep -e HW -e eth0 | head -1 | awk '{print \$NF}' | sed 's/://g' | tail -c 7`);
        $send['rack_loc'] = trim(`/opt/ethos/sbin/ethos-readconf loc`);
        $send['ip'] = trim(`/sbin/ifconfig | grep 'Bcast' | head -1 |  cut -d":" -f2 | cut -d" " -f1`);
        $send['mobo'] = trim(file_get_contents("/var/run/ethos/motherboard.file"));
        $send['lan_chip'] = trim(`/usr/bin/lspci -v | grep -Poi "(?<=Ethernet\scontroller\:\s)(.*)"`);
        $send['load'] = trim(`cat /proc/loadavg | cut -d" " -f3`);
        $send['ram'] = trim(`/usr/bin/free | head -2 | tail -1 | awk '{print \$2/1024/1024}' OFMT="%3.0f" | awk '{print \$1}'`);
        $send['cpu_temp'] = trim(file_get_contents("/var/run/ethos/cputemp.file"));
        $send['cpu_name'] = trim(`cat /proc/cpuinfo | grep 'model name' | awk -F": " '{print \$2}'`);
        $send['rofs'] = time() - trim(file_get_contents("/opt/ethos/etc/check-ro.file"));
        $send['drive_name'] = trim(`/opt/ethos/sbin/ethos-readdata driveinfo`);
        $send['freespace'] = round(trim(`/bin/df | grep '/dev/' | head -1 | awk '{print $4}'`) / 1024 / 1024, 1);
        $send['temp'] = trim(`/opt/ethos/sbin/ethos-readdata temps`);
        $send['version'] = trim(file_get_contents("/opt/ethos/etc/version"));
        $send['miner_secs'] = 0 + trim(`ps -eo pid,etime,command | grep $miner | grep -v grep | head -1 | awk '{print \$2}' |  /opt/ethos/bin/convert_time.awk`);
        $send['adl_error'] = trim(file_get_contents("/var/run/ethos/adl_error.file"));
        $send['proxy_problem'] = trim(file_get_contents("/var/run/ethos/proxy_error.file"));
        $send['updating'] = trim(file_get_contents("/var/run/ethos/updating.file"));
        $send['connected_displays'] = trim(`/opt/ethos/sbin/ethos-readdata connecteddisplays`);
        $send['resolution'] = trim(`/opt/ethos/sbin/ethos-readdata resolution`);
        $send['gethelp'] = trim(`tail -1 /var/log/gethelp.log`);
        $send['config_error'] = trim(`cat /var/run/ethos/config_mode.file`);
        $send['send_remote'] = trim(`cat /var/run/ethos/send_remote.file`);
        $send['autorebooted'] = trim(`cat /opt/ethos/etc/autorebooted.file`);
        $send['status'] = trim(`cat /var/run/ethos/status.file`);

        // gpu related info

        $send['driver'] = trim(`/opt/ethos/sbin/ethos-readconf driver`);
        $send['selected_gpus'] = trim(`/opt/ethos/sbin/ethos-readconf selectedgpus`);
        $send['gpus'] = $gpus;
        $send['fanrpm'] = trim(`/opt/ethos/sbin/ethos-readdata fanrpm | xargs | tr -s ' '`);
        $send['fanpercent'] = trim(`/opt/ethos/sbin/ethos-readdata fan | xargs | tr -s ' '`);
        $send['hash'] = trim(`tail -10 /var/run/ethos/miner_hashes.file | sort -V | tail -1 | tr ' ' '\n' | awk '{sum += \$1} END {print sum}'`);
        $send['miner'] = $miner;
        $send['miner_hashes'] = trim(`tail -10 /var/run/ethos/miner_hashes.file | sort -V | tail -1`);
        if(preg_match("/sgminer/",$miner)){
                $send['hwerrors'] = trim(`cat /var/run/ethos/hwerror.file`);
        }
        $send['models'] = trim(file_get_contents("/var/run/ethos/gpulist.file"));
        $send['bioses'] = trim(trim(`/opt/ethos/sbin/ethos-readdata bios | xargs | tr -s ' '`));
        $send['default_core'] = trim(file_get_contents("/var/run/ethos/defaultcore.file"));
        $send['default_mem'] = trim(file_get_contents("/var/run/ethos/defaultmem.file"));
        $send['vramsize'] = trim(file_get_contents("/var/run/ethos/vrams.file"));
        $send['core'] = trim(`/opt/ethos/sbin/ethos-readdata core | xargs | tr -s ' '`);
        $send['mem'] = trim(`/opt/ethos/sbin/ethos-readdata mem | xargs | tr -s ' '`);
        $send['memstates'] = trim(`/opt/ethos/sbin/ethos-readdata memstate | xargs | tr -s ' '`);
        $send['meminfo'] = trim(file_get_contents("/var/run/ethos/meminfo.file"));
        $send['voltage'] = trim(`/opt/ethos/sbin/ethos-readdata voltage | xargs | tr -s ' '`);
        $send['overheatedgpu'] = trim(file_get_contents("/var/run/ethos/overheatedgpu.file"));
        $send['throttled'] = trim(file_get_contents("/var/run/ethos/throttled.file"));
        $send['powertune'] = trim(`/opt/ethos/sbin/ethos-readdata powertune | xargs | tr -s ' '`);

        return $send;
}

function send_data()
{
        $send = get_stats();
        $private_hash = trim(file_get_contents("/var/run/ethos/private_hash.file"));
        $public_hash = trim(file_get_contents("/var/run/ethos/panel.file"));
         
        $hook = “http://gpu.website.com/api”
        $url = “http://gpu.website.com”

        $json = json_encode($send);
        $log = "";
        foreach($send as $key => $data) {
                $log.= "$key:$data\n";
        }
        $url_style = urlencode($json);
        $hostname = $send['hostname'];
        file("$hook?hostname=$hostname&url_style=$url_style&hash=$private_hash");
        return $log;
}
