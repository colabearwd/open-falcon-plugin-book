#!/usr/bin/python
#coding=utf-8

import ping
# pip install ping

if __name__ == '__main__':
    addr = "www.163.com"
    result = ping.quiet_ping(addr, timeout=2, count=5, psize=64)
    #loss_rate=result[0]
    #max_time=result[1]
    #average_time=result[2]
    print result
