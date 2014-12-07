#!/usr/bin/env python

import sys
import json
import urllib2

URL = 'http://localhost:8000/api/drive_historys/1/'


def push_location(lat=13.75, lnt=100.1667):
    data = json.dumps(
        {
            'latitude': lat,
            'longitude': lnt,
            'driver': 1,
            'vehicle': 1
        }
    )

    req = urllib2.Request(URL, data, {'Content-Type': 'application/json'})
    res = urllib2.urlopen(req)
    print res.msg, res.getcode()

if __name__ == '__main__':
    if len(sys.argv) == 1:
        push_location()
    else:
        push_location(sys.argv[1], sys.argv[2])