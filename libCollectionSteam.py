import urllib.request
def source_html(url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                             'AppleWebKit/537.11 (KHTML, like Gecko) '
                             'Chrome/23.0.1271.64 Safari/537.11',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
               'Accept-Encoding': 'none',
               'Accept-Language': 'en-US,en;q=0.8',
               'Connection': 'keep-alive'}
    return str(urllib.request.urlopen(urllib.request.Request(url=url, headers=headers)).read().decode("utf8"))
def Collection(collectionid):#1357125616
    myStr = source_html("https://steamcommunity.com/sharedfiles/filedetails/?id=" + str(collectionid))
    id = []
    pos = 1
    pos2 = 0
    findStr = ""
    url = ""
    char = ''
    b = False
    while pos != 0:
        pos = myStr.find("<div class=\"workshopItem\">", pos) + 1
        findStr = "<a href=\"https://steamcommunity.com/sharedfiles/filedetails/?id="
        pos = myStr.find(findStr, pos) + len(findStr)
        pos2 = myStr.find("\"><div class=\"workshopItemPreviewHolder", pos)
        url = myStr[pos:pos2]
        if url in id:
            break
        char = url[:1]
        for i in range(0, 10):
            if char == str(i):
                b = True
        if b == False:
            break
        if len(url) > 25:
            break
        id.append(url)
        #print(url)

    #modsFound = "Mods found:\t"
    #someInt = len(id)
    #modsFound += str(someInt)
    #print (modsFound)
    return id
def TitleWorkshop(appid):#1790667104
    data_html=source_html("https://steamcommunity.com/sharedfiles/filedetails/?id=" + str(appid))
    pos1=data_html.find('<div class="workshopItemTitle">')+len('<div class="workshopItemTitle">')
    Title=data_html[pos1:data_html.find('</div',pos1)]
    if len(Title)>100:
        return "Not Found"
    return Title