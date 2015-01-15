#!/usr/bin/env python
import sys
sys.path.insert(0, 'lib')
import urllib2
from bottle import Bottle, response, request, debug

app = Bottle()

# debug(True)

@app.get('/')
def home():
    return "home"

@app.get('/get')
def getStuff():
    url = request.query.url
    callback = request.query.callback

    resp = urllib2.urlopen(url)
    content = resp.read()

    response.headers['Access-Control-Allow-Origin'] = '*'

    if len(callback) > 0:
        response.content_type = 'application/x-javascript; charset=utf8'
        return (callback + '(' + content.decode('utf8')+')').encode('utf-8')
    else:
        response.content_type = 'application/json; charset=utf8'
        return content
