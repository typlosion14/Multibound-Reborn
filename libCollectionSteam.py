from CobraLib import source_html
import json

def Collection(collectionid):  # 1357125616
    myStr = source_html("https://steamcommunity.com/sharedfiles/filedetails/?id=" + str(collectionid))
    id = []
    pos = 1
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
    return id


def TitleWorkshop(appid):  # 1790667104
    print(appid)
    try:
        file=open('storage.json','r')
        storage=file.read()
        file.close()
    except:
        file=open('storage.json','w')
        storage='{}'
        file.write(storage)
        file.close()
    if str(appid) in storage:
        stockage=json.loads(storage)
        return stockage[str(appid)]
    else:
        data_html = source_html("https://steamcommunity.com/sharedfiles/filedetails/?id=" + str(appid))
        pos1 = data_html.find('<div class="workshopItemTitle">') + len('<div class="workshopItemTitle">')
        Title = data_html[pos1:data_html.find('</div', pos1)]
        if len(Title) > 100:
            return appid
        print("...")
        stockage = json.loads(storage)
        stockage[str(appid)]=Title
        stockage=json.dumps(stockage)
        file = open('storage.json','w')
        file.write(stockage)
        file.close()
        if appid.endswith('.pak'):
            return appid+' , '+Title
        return Title

def MultipleTitleWorkshop(appid):
    if 'None' in appid:
        return 'None'
    sortie=[]
    for i in range(len(appid)):
        sortie.append(TitleWorkshop(appid[i]))
    return sortie
