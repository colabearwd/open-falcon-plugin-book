#!/usr/bin/python
#!-*- coding:utf8 -*-

import requests
import time
import json
import random
import Adafruit_DHT

ts = int(time.time())
sensor1 = Adafruit_DHT.DHT11
humidity1, temperature1 = Adafruit_DHT.read_retry(sensor1, 4)
#print humidity1,temperature1

payload = [
            {
                        "endpoint": "Master",
                        "metric": "temperature",
                        "timestamp": ts,
                        "step": 60,
                        "value": temperature1,
                        "counterType": "GAUGE",
                        "tags": "facility=raspberry",
            },

            {
                        "endpoint": "Master",
                        "metric": "humidity",
                        "timestamp": ts,
                        "step": 60,
                        "value": humidity1,
                        "counterType": "GAUGE",
                        "tags": "facility=raspberry",
            },
        ]

r = requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(payload))
print r
