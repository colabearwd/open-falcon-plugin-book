#!/usr/bin/python
#coding=utf-8

import requests
import time 
import json
import random
import ping
# pip install ping

if __name__ == '__main__':
    addr = "www.163.com"
    result = ping.quiet_ping(addr, timeout=2, count=5, psize=64)
    loss_rate=result[0]
    max_time=result[1]
    average_time=result[2]
    ts=int(time.time())
    payload = [
	
	{
    "metric": "ping.loss_rate",
    "endpoint": "ubuntu-pi-test",
    "tags": "test=ubuntupiwd",
    "value": loss_rate,
    "timestamp": ts,
    "counterType": "GAUGE",
    "step": 60
	},
	{
    "metric": "ping.max_time",
    "endpoint": "ubuntu-pi-test",
    "tags": "test=ubuntupiwd",
    "value": max_time,
    "timestamp": ts,
    "counterType": "GAUGE",
    "step": 60
	},
	{
    "metric": "ping.average_time",
    "endpoint": "ubuntu-pi-test",
    "tags": "test=ubuntupiwd",
    "value": average_time,
    "timestamp": ts,
    "counterType": "GAUGE",
    "step": 60
	}

    ]
	




    r = requests.post("http://127.0.0.1:1988/v1/push",data=json.dumps(payload))
    print r.text
    print json.dumps(payload)
    print result
