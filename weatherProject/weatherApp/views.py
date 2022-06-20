import urllib.request
import json

from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
from django.views import View
# from .phantich import * 
from .tinhtoan import *
import http
import js2py
from .views import *

def xltk_chung(request):
# thongKeChung(_Month, _Year, Type_PT):
    year = int(request.POST.get('year'))
    month = int(request.POST.get('month'))
    tkType = request.POST.get('tkType')
    
    if month==0 or year==0 or tkType==0:
        return render(request, "main/thongkechung.html",None)
    else:
        df = thongKeChung(month, year, tkType)
        df.to_csv('weatherApp/static/dulieu.csv')       
        df.to_html('weatherApp/templates/main/dulieuhtml.html')
        return render(request, "main/thongkechung_result.html",None)
  


def xltk_ngay(request):
# def thongKeNgay(id_PT, _Day, _Month, _Year):
    day = int(request.POST.get('day'))
    year = int(request.POST.get('year'))
    month = int(request.POST.get('month'))
    tinh = int(request.POST.get('idPT'))
    
    if day==0 or year==0 or month==0 or tinh==0:
        return render(request, "main/thongkengay.html",None)
    else:
        df = thongKeNgay(tinh, day, month, year)
        df.to_csv('weatherApp/static/dulieu.csv')       
        df.to_html('weatherApp/templates/main/dulieuhtml.html')
        return render(request, "main/thongkengay_result.html",None)

def xltk_thang(request):
#  thongKeThang(id_PT, _Month, _Year, Type_PT):
    year = int(request.POST.get('year'))
    month = int(request.POST.get('month'))
    tinh = int(request.POST.get('idPT'))
    tkType = request.POST.get('tkType')

    if year==0 or month==0 or tinh==0 or tkType==0:
        return render(request, "main/thongkethang.html",None)
    else:
        df = thongKeThang(tinh, month, year, tkType)
        df.to_csv('weatherApp/static/dulieu.csv')       
        df.to_html('weatherApp/templates/main/dulieuhtml.html')
        return render(request, "main/thongkethang_result.html",None)

def xltk_nam(request):
#  thongKeNam(id_PT, _Year, Type_PT):
    quy = int(request.POST.get('quy'))
    year = int(request.POST.get('year'))
    tinh = int(request.POST.get('idPT'))
    tkType = request.POST.get('tkType')
   
    
    if quy != 0:
        if year==0 or tinh==0 or tkType==0:
            return render(request, "main/thongkenam.html",None)
        else:
            df = thongKeQuy(tinh, quy, year, tkType)
            df.to_csv('weatherApp/static/dulieu.csv')       
            df.to_html('weatherApp/templates/main/dulieuhtml.html')
            return render(request, "main/thongkenam_result.html",None)
    else:
        if year==0 or tinh==0 or tkType==0:
            return render(request, "main/thongkenam.html",None)
        else:
            df = thongKeNam(tinh, year, tkType)
            df.to_csv('weatherApp/static/dulieu.csv')       
            df.to_html('weatherApp/templates/main/dulieuhtml.html')
            return render(request, "main/thongkenam_result.html",None)


from urllib.parse import quote
    
def datalist(location):
    url = urllib.request.urlopen('http://api.weatherapi.com/v1/forecast.json?key=9ee35465bdf14965b16140311221505&q=' + location + '&days=3&aqi=no&alerts=no&lang=vi').read()

    source = url
    list_of_data = json.loads(source)
    data = {
        "location": str(list_of_data['location']['name']),


        "temp": str(list_of_data['current']['temp_c']) + ' °C',
        "pressure": str(list_of_data['current']['pressure_mb']) + ' mb',
        "humidity": str(list_of_data['current']['humidity']) + '%',
        'wind_mph': str(list_of_data['current']['wind_mph']) + ' km/h',
        'uv': str(list_of_data['current']['uv']),
        'icon': list_of_data['current']['condition']['icon'],
        'status': list_of_data['current']['condition']['text'],
        'precip_mm': str(list_of_data['current']['precip_mm']) + ' m',
        'visibility': str(list_of_data['current']['vis_km']) + ' km',


# API 3 ngày tới

        "date_day1": str(list_of_data['forecast']['forecastday'][0]['date']),
        "date_day2": str(list_of_data['forecast']['forecastday'][1]['date']),
        "date_day3": str(list_of_data['forecast']['forecastday'][2]['date']),

        "mintemp_day1": str(list_of_data['forecast']['forecastday'][0]['day']['mintemp_c']) + ' °C',
        "mintemp_day2": str(list_of_data['forecast']['forecastday'][1]['day']['mintemp_c']) + ' °C',
        "mintemp_day3": str(list_of_data['forecast']['forecastday'][2]['day']['mintemp_c']) + ' °C',

        "maxtemp_day1": str(list_of_data['forecast']['forecastday'][0]['day']['maxtemp_c']) + ' °C',
        "maxtemp_day2": str(list_of_data['forecast']['forecastday'][1]['day']['maxtemp_c']) + ' °C',
        "maxtemp_day3": str(list_of_data['forecast']['forecastday'][2]['day']['maxtemp_c']) + ' °C',

        "status_day1": str(list_of_data['forecast']['forecastday'][0]['day']['condition']['text']),
        "status_day2": str(list_of_data['forecast']['forecastday'][1]['day']['condition']['text']),
        "status_day3": str(list_of_data['forecast']['forecastday'][2]['day']['condition']['text']),

        "icon_day1": str(list_of_data['forecast']['forecastday'][0]['day']['condition']['icon']),
        "icon_day2": str(list_of_data['forecast']['forecastday'][1]['day']['condition']['icon']),
        "icon_day3": str(list_of_data['forecast']['forecastday'][2]['day']['condition']['icon']),
    }
    return data
    

def index(request):
    data = datalist('ha+noi')
    return render(request, "main/main.html", data)

def index2(request):
    return render(request, "main/thongkechung.html",None)

def index3(request):
    return render(request, "main/thongkengay.html",None)

def index4(request):
    return render(request, "main/thongkethang.html",None)

def index5(request):
    return render(request, "main/thongkenam.html",None)

def index6(request):
    return render(request, "main/xemdulieu.html",None)


def angiang(request):
    data = datalist('an+giang')
    return render(request, "main/main.html", data)

def brvt(request):
    data = datalist('vung+tau')
    return render(request, "main/main.html", data)

def bacgiang(request):
    data = datalist('bac+giang')
    return render(request, "main/main.html", data)

def backan(request):
    data = datalist('bac+kan')
    return render(request, "main/main.html", data)

def baclieu(request):
    data = datalist('bac+lieu')
    return render(request, "main/main.html", data)

def bacninh(request):
    data = datalist('bac+ninh')
    return render(request, "main/main.html", data)

def bentre(request):
    data = datalist('ben+tre')
    return render(request, "main/main.html", data)

def binhdinh(request):
    data = datalist('binh+dinh')
    return render(request, "main/main.html", data)

def binhduong(request):
    data = datalist('binh+duong')
    return render(request, "main/main.html", data)

def binhphuoc(request):
    data = datalist('binh+phuoc')
    return render(request, "main/main.html", data)

def binhthuan(request):
    data = datalist('binh+thuan')
    return render(request, "main/main.html", data)

def camau(request):
    data = datalist('ca+mau')
    return render(request, "main/main.html", data)

def cantho(request):
    data = datalist('can+tho')
    return render(request, "main/main.html", data)

def caobang(request):
    data = datalist('cao+bang')
    return render(request, "main/main.html", data)

def danang(request):
    data = datalist('da+nang')
    return render(request, "main/main.html", data)

def daklak(request):
    data = datalist('dac+lac')
    return render(request, "main/main.html", data)

def daknong(request):
    data = datalist('dak+nong')
    return render(request, "main/main.html", data)

def dienbien(request):
    data = datalist('dien+bien')
    return render(request, "main/main.html", data)

def dongnai(request):
    data = datalist('dong+nai')
    return render(request, "main/main.html", data)

def dongthap(request):
    data = datalist('dong+thap')
    return render(request, "main/main.html", data)

def gialai(request):
    data = datalist('gia+lai')
    return render(request, "main/main.html", data)

def hagiang(request):
    data = datalist('ha+giang')
    return render(request, "main/main.html", data)

def hanam(request):
    data = datalist('ha+nam')
    return render(request, "main/main.html", data)

def hanoi(request):
    data = datalist('ha+noi')
    return render(request, "main/main.html", data)

def hatinh(request):
    data = datalist('ha+tinh')
    return render(request, "main/main.html", data)

def haiduong(request):
    data = datalist('hai+duong')
    return render(request, "main/main.html", data)

def haiphong(request):
    data = datalist('hai+phong')
    return render(request, "main/main.html", data)

def haugiang(request):
    data = datalist('hau+giang')
    return render(request, "main/main.html", data)

def hoabinh(request):
    data = datalist('hoa+binh')
    return render(request, "main/main.html", data)

def hungyen(request):
    data = datalist('hungyen')
    return render(request, "main/main.html", data)

def khanhhoa(request):
    data = datalist('khanh+hoa')
    return render(request, "main/main.html", data)

def kiengiang(request):
    data = datalist('kien+giang')
    return render(request, "main/main.html", data)

def kontum(request):
    data = datalist('kontum')
    return render(request, "main/main.html", data)

def laichau(request):
    data = datalist('lai+chau')
    return render(request, "main/main.html", data)

def lamdong(request):
    data = datalist('lam+dong')
    return render(request, "main/main.html", data)

def langson(request):
    data = datalist('lang+son')
    return render(request, "main/main.html", data)

def laocai(request):
    data = datalist('lao+cai')
    return render(request, "main/main.html", data)

def longan(request):
    data = datalist('long+an')
    return render(request, "main/main.html", data)

def namdinh(request):
    data = datalist('nam+dinh')
    return render(request, "main/main.html", data)

def nghean(request):
    data = datalist('nghe+an')
    return render(request, "main/main.html", data)

def ninhbinh(request):
    data = datalist('ninh+binh')
    return render(request, "main/main.html", data)

def ninhthuan(request):
    data = datalist('ninh+thuan')
    return render(request, "main/main.html", data)

def phutho(request):
    data = datalist('phu+tho')
    return render(request, "main/main.html", data)

def phuyen(request):
    data = datalist('phu+yen')
    return render(request, "main/main.html", data)

def quangbinh(request):
    data = datalist('quang+binh')
    return render(request, "main/main.html", data)

def quangnam(request):
    data = datalist('quang+nam')
    return render(request, "main/main.html", data)

def quangngai(request):
    data = datalist('quang+ngai')
    return render(request, "main/main.html", data)

def quangninh(request):
    data = datalist('quang+ninh')
    return render(request, "main/main.html", data)

def quangtri(request):
    data = datalist('quang+tri')
    return render(request, "main/main.html", data)

def soctrang(request):
    data = datalist('soc+trang')
    return render(request, "main/main.html", data)

def sonla(request):
    data = datalist('son+la')
    return render(request, "main/main.html", data)

def tayninh(request):
    data = datalist('tay+ninh')
    return render(request, "main/main.html", data)

def thaibinh(request):
    data = datalist('thai+binh')
    return render(request, "main/main.html", data)

def thainguyen(request):
    data = datalist('thai+nguyen')
    return render(request, "main/main.html", data)

def thanhhoa(request):
    data = datalist('thanh+hoa')
    return render(request, "main/main.html", data)

def thuathienhue(request):
    data = datalist('thua+thien+hue')
    return render(request, "main/main.html", data)

def tiengiang(request):
    data = datalist('tien+giang')
    return render(request, "main/main.html", data)

def tiengiang(request):
    data = datalist('tien+giang')
    return render(request, "main/main.html", data)

def hcm(request):
    data = datalist('ho+chi+minh')
    return render(request, "main/main.html", data)

def travinh(request):
    data = datalist('tra+vinh')
    return render(request, "main/main.html", data)

def tuyenquang(request):
    data = datalist('tuyen+quang')
    return render(request, "main/main.html", data)

def vinhlong(request):
    data = datalist('vinh+long')
    return render(request, "main/main.html", data)

def vinhphuc(request):
    data = datalist('vinh+phuc')
    return render(request, "main/main.html", data)

def yenbai(request):
    data = datalist('yen+bai')
    return render(request, "main/main.html", data)


