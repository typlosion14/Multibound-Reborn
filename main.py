import configparser as cp
import os
import shutil
from CobraLib import directSearch
from configStorage import Config, Translate, init


def ChooseYourInstance(dic):
    try:
        print(Translate.ChooseInstance())
        for i in range(0, len(dic)):
            print(str(i + 1) + " " + dic['Instance' + str(i + 1)][0])
    except:
        return Translate.ErrorInstance()
    try:
        choice = int(input(Translate.ChooseInstance()))
        if choice not in range(1, len(dic) + 1):
            return ChooseYourInstance(dic)
        else:
            return Translate.loading(), choice, dic
    except:
        return ChooseYourInstance(dic)


def LoadingInstance():
    config = cp.ConfigParser()
    config.read_file(open('config.ini'))
    dic = {}
    try:
        for i in range(0, Config.InstanceNumber):
            dic['Instance' + str(i + 1)] = config.get('INSTANCE' + str(i + 1), 'Name'), config.get(
                'INSTANCE' + str(i + 1), 'workshoplist'), config.get('INSTANCE' + str(i + 1), 'ModsList')
    except:
        return Translate.ErrorInstance()
    return ChooseYourInstance(dic)


def InstanceAppli(ch, dic):
    InstanceLoad = dic['Instance' + str(ch)]
    Workshop = InstanceLoad[1].split(',')
    ModLoad = InstanceLoad[2].split(',')
    try:
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
    try:
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
    os.system('"'+Config.SteamAppsPath + '\\common\Starbound\win64\starbound.exe"')
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
    return Translate.LaunchStarbound()


def ListeCreator(dic):
    AllName = []
    for i in range(0, len(dic)):
        AllName.append(dic['Instance' + str(i + 1)][0])
    return AllName


print(init())
inst = LoadingInstance()
print(inst[0])
print(InstanceAppli(inst[1], inst[2]))
# Todo : Inteface Graphique avec Nom et Image
