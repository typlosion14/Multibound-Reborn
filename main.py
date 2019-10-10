import configparser as cp
import webbrowser
import os
import json
import shutil
from CobraLib import directSearch,importjson
from configStorage import Config, Translate, init


def ChooseYourInstance(dic):
    try:
        for i in range(0, len(dic)):
            print(str(i + 1) + " " + dic['Instance' + str(i + 1)][0])
    except:
        return Translate.ErrorInstance()
    try:
        choice = int(input(Translate.ChooseInstanceMain()))
        if choice not in range(1, len(dic) + 1):
            return ChooseYourInstance(dic)
        else:
            return Translate.loading(), choice, dic
    except:
        return ChooseYourInstance(dic)

def CheckUpdate():
    DicGit=json.loads(importjson("https://api.github.com/repos/typlosion14/Multibound-Reborn/releases/latest","77a0b70044d0f39e64f08097a21f5a750d5b1323 "))
    VersionGit=DicGit['tag_name']
    config = cp.ConfigParser()
    config.read_file(open('config.ini'))
    ActualVersion=Config.Version
    if ActualVersion!=VersionGit and ActualVersion[0]<=VersionGit[0] and ActualVersion[2]<=VersionGit[2] and ActualVersion[4]<=VersionGit[4]:
        print(Translate.NeedUpdate())
        try:
            ch=int(input(Translate.DownloadChoice()))
        except:
            return
        if ch==1:
            UrlGit = DicGit['assets']['browser_download_url']
            print(Translate.loading())
            webbrowser.open_new(UrlGit)
            input(Translate.PleaseInstall())
            exit()
    return Translate.NoUpdateFound()

def LoadingInstance():
    config = cp.ConfigParser()
    config.read_file(open('config.ini'))
    dic = {}
    try:
        for i in range(0, Config.InstanceNumber):
            try:
                dic['Instance' + str(i + 1)] = config.get('INSTANCE' + str(i + 1), 'Name'), config.get(
                'INSTANCE' + str(i + 1), 'workshoplist'), config.get('INSTANCE' + str(i + 1), 'ModsList'),config.get('INSTANCE' + str(i + 1), 'saveLocation')
            except:
                dic['Instance' + str(i + 1)] = config.get('INSTANCE' + str(i + 1), 'Name'), config.get(
                    'INSTANCE' + str(i + 1), 'workshoplist'), config.get('INSTANCE' + str(i + 1),'ModsList'), 'default'
    except:
        return Translate.ErrorInstance()
    return ChooseYourInstance(dic)


def InstanceAppli(ch, dic):
    InstanceLoad = dic['Instance' + str(ch)]
    Workshop = InstanceLoad[1].split(',')
    ModLoad = InstanceLoad[2].split(',')
    saveLocation = InstanceLoad[3]
    try: #Changer les mods du workshop
        direc = directSearch(Config.SteamAppsPath + "\\workshop\content\\211820")
        os.chdir(Config.SteamAppsPath + "\\workshop\content\\211820")
        for i in range(0, len(direc)):
            if not direc[i].startswith("Disabled."):
                VerifDirec=direc[i]
                print(VerifDirec)
                for y in range(0,len(direc)):
                    if direc[y].startswith("Disabled.") and direc[y].endswith(VerifDirec):
                        shutil.rmtree(Config.SteamAppsPath + "\\workshop\content\\211820\\Disabled."+VerifDirec)
            if direc[i] not in Workshop and "Disabled." not in direc[i]:
                os.rename(direc[i], "Disabled." + str(direc[i]))
        for i in range(0, len(Workshop)):
            if ("Disabled." + Workshop[i]) in direc:
                os.rename("Disabled." + Workshop[i], Workshop[i])
    except:

        return Translate.WorkshopError()
    try: #changer les mods
        direc = directSearch(Config.SteamAppsPath + "\\common\Starbound\mods")
        os.chdir(Config.SteamAppsPath + "\\common\Starbound\mods")
        for i in range(0, len(direc)):
            if not direc[i].startswith(".Disabled."):
                VerifDirec = direc[i]
                for y in range(0, len(direc)):
                    if direc[y].startswith(".Disabled.") and direc[y].endswith(VerifDirec):
                        shutil.rmtree(Config.SteamAppsPath + "\\common\Starbound\mods\\.Disabled." + VerifDirec)
            if direc[i] not in ModLoad and "Disabled." not in direc[i]:
                os.rename(direc[i], ".Disabled." + str(direc[i]))
        for i in range(0, len(ModLoad)):
            if (".Disabled." + ModLoad[i]) in direc:
                os.rename(".Disabled." + ModLoad[i], ModLoad[i])
    except:
        return Translate.ModError()
    if saveLocation!="default":
        try:
            os.makedirs(Config.SteamAppsPath + "\\common\Starbound\InstanceSave\\"+str(ch))
        except:
            print('Save found!')
        try:
            os.replace(Config.SteamAppsPath + "\\common\Starbound\\storage",Config.SteamAppsPath + "\\common\Starbound\InstanceSave\\storage")
            os.replace(Config.SteamAppsPath + "\\common\Starbound\InstanceSave\\"+str(ch),Config.SteamAppsPath + "\\common\Starbound\\storage")
        except:
            return Translate.BugMoveFile()
    print(Translate.LaunchStarbound())
    os.system('"'+Config.SteamAppsPath + '\\common\Starbound\win64\starbound.exe"')#Lance le jeu
    #Annule les changements
    direc = directSearch(Config.SteamAppsPath + "\\workshop\content\\211820")
    os.chdir(Config.SteamAppsPath + "\\workshop\content\\211820")
    for i in range(0, len(direc)):
        if direc[i].startswith("Disabled."):
            NewName=str(direc[i][direc[i].find('.')+1:])
            os.rename(direc[i], NewName)
    direc = directSearch(Config.SteamAppsPath + "\\common\Starbound\mods")
    os.chdir(Config.SteamAppsPath + "\\common\Starbound\mods")
    for i in range(0, len(direc)):
        if direc[i].startswith(".Disabled."):
            NewName=str(direc[i][direc[i].find('.Disabled.')+len(".Disabled."):])
            os.rename(direc[i], NewName)
    #SaveLocation
    if saveLocation!="default":
        os.replace(Config.SteamAppsPath + "\\common\Starbound\\storage",Config.SteamAppsPath + "\\common\Starbound\InstanceSave\\"+str(ch))
        os.replace(Config.SteamAppsPath + "\\common\Starbound\InstanceSave\\storage",Config.SteamAppsPath + "\\common\Starbound\\storage")
    return "See you later!"


def ListeCreator(dic):
    AllName = []
    for i in range(0, len(dic)):
        AllName.append(dic['Instance' + str(i + 1)][0])
    return AllName

CheckUpdate()
print(init())
inst = LoadingInstance()
print(inst[0])
print(InstanceAppli(inst[1], inst[2]))
# Todo : Inteface Graphique avec Nom et Image
