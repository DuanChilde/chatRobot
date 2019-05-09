#!/usr/bin/env python
# -*- coding: utf-8 -*-


# http://toy.weather.com.cn/SearchBox/searchBox?_=1362892474803&language=zh&keyword=%E5%8C%97%E4%BA%AC

from urllib import request
import sys
import json

ENCODING = 'utf-8'


def queryLocation(term):
    term = term.encode(ENCODING) if type(term) == "unicode" else term
    url = "http://toy.weather.com.cn/SearchBox/searchBox?language=zh&keyword=" + request.quote(term)
    #resp = urllib.urlopen(url)
    #data = json.load(resp)
    #if not data:
    #    print u"找不到地点".encode(ENCODING)
    #for d in data["i"]:
    #    code = d['i']
    #    break
    code = "101200101"
    return code

def queryRealTimeWeatherInfo(code):
    url = "http://t.weather.sojson.com/api/weather/city/%s" % code
    resp = request.urlopen(url)
    data = json.load(resp)
    if not data:
        print(u"天气预报还没出来".encode(ENCODING))
    return data

def showRealTimeWeatherInfo(info):
    template = u"%s %s 天气实况: 气温%s℃, 空气质量%s，湿度%s" % (info['cityInfo']['city'],info['time'],info['data']['wendu'],info['data']['quality'],info['data']['shidu'])
    print(template)


def main():
    #assert len(sys.argv) >= 3
    function = sys.argv[1]
    term = ''.join(sys.argv[2:])
    if function == 'realtime':
        # 实时
        showRealTimeWeatherInfo(queryRealTimeWeatherInfo(queryLocation(term)))

if __name__ == '__main__':
    main()
