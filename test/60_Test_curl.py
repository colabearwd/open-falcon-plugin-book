#!/usr/bin/python
#coding=utf-8

import requests
import time
import json
import random
import ping
import commands
# pip install ping

def curl(url):
    cmd = "curl -o /dev/null -s -w %{http_code}:%{http_connect}:%{content_type}:%{time_namelookup}:%{time_redirect}:%{time_pretransfer}:%{time_connect}:%{time_starttransfer}:%{time_total}:%{speed_download} " + url
    status, output = commands.getstatusoutput(cmd)
    if status != 0:
        return False, "Call Curl Error"
    return True, output.split(":")

if __name__ == '__main__':
    addr = "www.163.com"
	
	success, result = curl("addr")
	
    print success
    print result
	
	http_code=result[0]
	http_connect=result[1]
	content_type=result[2]
	time_namelookup=result[3]
	time_redirect=result[4]
	time_pretransfer=result[5]
	time_connect=result[6]
	time_starttransfer=result[7]
	time_total=result[8]
	speed_download=result[9]
	
    ts=int(time.time())
    payload = [
        {
    "metric": "curl.http_code",
    "endpoint": "ubuntu-pi-test",
    "tags": "test=ubuntu-curl",
    "value": http_code,
    "timestamp": ts,
    "counterType": "GAUGE",
    "step": 60
        },
        {
    "metric": "curl.http_connect",
    "endpoint": "ubuntu-pi-test",
    "tags": "test=ubuntu-curl",
    "value": http_connect,
    "timestamp": ts,
    "counterType": "GAUGE",
    "step": 60
        },
        {
    "metric": "curl.content_type",
    "endpoint": "ubuntu-pi-test",
    "tags": "test=ubuntu-curl",
    "value": content_type,
    "timestamp": ts,
    "counterType": "GAUGE",
    "step": 60
        }
    "metric": "curl.time_namelookup",
    "endpoint": "ubuntu-pi-test",
    "tags": "test=ubuntu-curl",
    "value": time_namelookup,
    "timestamp": ts,
    "counterType": "GAUGE",
    "step": 60
        },
        {
    "metric": "curl.time_redirect",
    "endpoint": "ubuntu-pi-test",
    "tags": "test=ubuntu-curl",
    "value": time_redirect,
    "timestamp": ts,
    "counterType": "GAUGE",
    "step": 60
        },
        {
    "metric": "curl.time_pretransfer",
    "endpoint": "ubuntu-pi-test",
    "tags": "test=ubuntu-curl",
    "value": time_pretransfer,
    "timestamp": ts,
    "counterType": "GAUGE",
    "step": 60
        }
    "metric": "curl.time_connect",
    "endpoint": "ubuntu-pi-test",
    "tags": "test=ubuntu-curl",
    "value": time_connect,
    "timestamp": ts,
    "counterType": "GAUGE",
    "step": 60
        },
        {
    "metric": "curl.time_starttransfer",
    "endpoint": "ubuntu-pi-test",
    "tags": "test=ubuntu-curl",
    "value": time_starttransfer,
    "timestamp": ts,
    "counterType": "GAUGE",
    "step": 60
        },
        {
    "metric": "curl.time_total",
    "endpoint": "ubuntu-pi-test",
    "tags": "test=ubuntu-curl",
    "value": time_total,
    "timestamp": ts,
    "counterType": "GAUGE",
    "step": 60
        }
        {
    "metric": "curl.speed_download",
    "endpoint": "ubuntu-pi-test",
    "tags": "test=ubuntu-curl",
    "value": speed_download,
    "timestamp": ts,
    "counterType": "GAUGE",
    "step": 60
        }
    ]

    r = requests.post("http://127.0.0.1:1988/v1/push",data=json.dumps(payload))
    print r.text
    print json.dumps(payload)
    print result
