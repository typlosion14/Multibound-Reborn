import os
from urllib.request import urlopen, Request


def source_html(url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                             'AppleWebKit/537.11 (KHTML, like Gecko) '
                             'Chrome/23.0.1271.64 Safari/537.11',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
               'Accept-Encoding': 'none',
               'Accept-Language': 'en-US,en;q=0.8',
               'Connection': 'keep-alive'}
    return str(urlopen(Request(url=url, headers=headers)).read())


def directSearch(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]


def ListToString(list):
    string = ''
    for i in range(len(list)):
        if i != len(list) - 1:
            string = string + str(list[i]) + ','
        else:
            string = string + str(list[i])
    return string


def StringToList(string):  # convertString
    list = []
    pos1 = 0
    for i in range(string.count(",")):
        list.append(string[pos1:string.index(",", pos1)])
        pos1 = string.index(",", pos1) + 1
    list.append(string[pos1:])
    return list
def StringToDict(string):
    #{"id":"5d1e07a0a38e4a4fdd7cefca","activation":"2019-07-19T13:00:00.000Z","startString":"-19m 10s","expiry":"2019-07-21T13:00:00.000Z","active":true,"character":"Baro Ki'Teer","location":"Larunda Relay (Mercury)","inventory":[{"item":"Kavat Bust","ducats":220,"credits":250000},{"item":"Scimitar Cydonia Skin","ducats":375,"credits":340000},{"item":"Jolt","ducats":300,"credits":150000},{"item":"Voltaic Strike","ducats":300,"credits":150000},{"item":"High Voltage","ducats":300,"credits":150000},{"item":"Shell Shock","ducats":300,"credits":150000},{"item":"Primed Quickdraw","ducats":375,"credits":120000},{"item":"Primed Heavy Trauma","ducats":350,"credits":100000},{"item":"Prova Vandal","ducats":410,"credits":250000},{"item":"Quanta Vandal","ducats":450,"credits":300000},{"item":"Quanta Aufeis Skin","ducats":300,"credits":300000},{"item":"Ki'Teer Diax Syandana","ducats":325,"credits":450000},{"item":"Ki'Teer Foros Shoulder Plates","ducats":310,"credits":100000},{"item":"Ki'Teer Foros Chest Plate","ducats":175,"credits":200000},{"item":"Ki'Teer Foros Leg Plates","ducats":225,"credits":150000},{"item":"Prisma Companion Poster","ducats":90,"credits":110000},{"item":"Pyra Sugatra","ducats":100,"credits":200000},{"item":"Tigris Elixis Skin","ducats":300,"credits":275000},{"item":"Sonicor Exilis Skin","ducats":380,"credits":175000},{"item":"Liset Prisma Skin","ducats":120,"credits":150000},{"item":"Ki'Teer Atmos Diadem","ducats":525,"credits":375000},{"item":"Baro Ki'Teer Glyph","ducats":80,"credits":50000},{"item":"Eminence","ducats":220,"credits":220000},{"item":"Corrupted Bombard Specter Blueprint","ducats":100,"credits":50000},{"item":"Sands Of Inaros Blueprint","ducats":100,"credits":25000}],"psId":"5d1e07a0a38e4a4fdd7cefca25","endString":"1d 23h 40m 49s"}
    #{"id":"5d1e07a0a38e4a4fdd7cefca","activation":"2019-07-19T13:00:00.000Z","startString":"24m 19s","expiry":"2019-07-21T13:00:00.000Z","active":false,"character":"Baro Ki\'Teer","location":"Larunda Relay (Mercury)","inventory":[],"psId":"5d1e07a0a38e4a4fdd7cefca0","endString":"2d 24m 19s"}
    dic={}
    pos1=0
    while string[pos1:].count(",")!=0:
        delimiter1=string[pos1+1]
        key=string[pos1+2:string.find(delimiter1,pos1+2)]
        pos1=string.find(delimiter1+key+delimiter1+":")+len(delimiter1+key+delimiter1+":")
        delimiter2=string[pos1:pos1+1]
        if string[pos1:pos1+2]=="[{":
            data=string[pos1:string.find("}]")+1]
            pos1=pos1+len(data)+1
        elif delimiter2 in ('"', "'"):
            data=string[string.find(delimiter2,pos1)+1:string.find(delimiter2,pos1+2)]
            pos1 = string.find(",", pos1)
        else:
            data=string[pos1:string.find(",",pos1)]
            pos1 = string.find(",", pos1)
        dic[key]=data
    return dic
def StringToDate(string):#2019-07-22T00:00:00.000Z
    Year=string[:4]
    Month=string[5:7]
    Day=string[8:10]
    Hour=string[11:13]
    Minute=string[14:16]
    return Year,Month,Day,Hour,Minute