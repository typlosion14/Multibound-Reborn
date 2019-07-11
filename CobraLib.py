import os
from urllib.request import urlopen, Request

#Made by Typlosion14
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
