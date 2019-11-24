import configparser as cp
import json
import tkinter as tk
from tkinter import filedialog
from libCollectionSteam import Collection
from configStorage import Translate,Config,pageShow,init
from CobraLib import directSearch,os,StringToList,ListToString,pakSearch

def savelocation(dic,ch):
    ConfigSaveLocation = dic['Instance' + str(ch)][3]
    try:
        choice = int(input(Translate.saveLocation(ConfigSaveLocation)))
    except:
        return savelocation(dic,ch)
    if choice==1:
        config = cp.ConfigParser()
        config.read_file(open('config.ini'))
        if ConfigSaveLocation == 'default':
            config.set('INSTANCE' + str(ch), "savelocation", "instance")
        else:
            SaveList='player','universe'
            for i in range(len(SaveList)):
                if "." in SaveList[i]:
                    os.replace(Config.SteamAppsPath + "\\common\Starbound\\InstanceSave\\"+ str(ch)+"\\"+SaveList[i],Config.SteamAppsPath + "\\common\Starbound\\storage\\"+SaveList[i])
                else:
                    SaveList2=os.listdir(Config.SteamAppsPath + "\\common\Starbound\\InstanceSave\\"+ str(ch)+"\\"+SaveList[i])
                    for y in range(len(SaveList2)):
                        os.replace(
                            Config.SteamAppsPath + "\\common\Starbound\\InstanceSave\\" + str(ch) + "\\" + SaveList[i]+"\\"+SaveList2[y],
                            Config.SteamAppsPath + "\\common\Starbound\\storage\\" + SaveList[i]+"\\"+SaveList2[y])
            try:
                os.remove(Config.SteamAppsPath + "\\common\Starbound\\InstanceSave\\" + str(ch))
            except:
                print("Can't delete "+Config.SteamAppsPath + "\\common\Starbound\\InstanceSave\\" + str(ch)+'\nNot a problem, continue...')
            config.set('INSTANCE' + str(ch), "savelocation", "default")
        with open('config.ini', 'w') as settings:
            config.write(settings)
    return ModifyYourInstance(refreshdic(), ch)



def deletethis(json):
    for i in range(json.count(' //')):
        jsonpart1=json[:json.find(' //')-2]
        jsonpart2=json[json.find('\n',json.find(' //'))+1:]
        json=jsonpart1+jsonpart2
    verif=json[json.find(']\n'):]
    if '}' in verif:
        return (json).replace('workshopId','id')
    else:
        return (json+'}').replace('workshopId', 'id')

def CreateInstance():
    NameInstance = str(input(Translate.NameInstance()))
    if NameInstance == '' or NameInstance == 'None':
        NameInstance = 'NewInstance'
    config = cp.ConfigParser()
    config.read_file(open('config.ini'))
    config['INSTANCE' + str(Config.InstanceNumber + 1)] = {'Name': NameInstance, 'modslist': 'None',
                                                           'workshoplist': 'None','saveLocation':'default'}
    Config.InstanceNumber = Config.InstanceNumber + 1
    with open('config.ini', 'w') as settings:
        config.write(settings)
    return ChooseYourInstance(refreshdic())


def ChoiceWhatToDo():
    try:
        ch = int(input(Translate.Choice()))
    except:
        return ChoiceWhatToDo()
    if ch == 1:
        os.system("cls")
        return LoadingInstance()
    elif ch == 2:
        os.system("cls")
        return CreateInstance()
    elif ch == 3:
        os.system("cls")
        return ConfigFile()
    elif ch == 4:
        os.system("cls")
        return CleanerConfig()
    elif ch == 5:
        os.system("cls")
        return ImportInstance()
    else:
        os.system("cls")
        return ChoiceWhatToDo()

def ImportInstance():
    print(Translate.Import())
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    if file_path.endswith("instance.json"):
        ListWorkshop=[]
        print(Translate.loading())
        file1=open(file_path,"r")
        data=file1.read()
        file1.close()
        print(deletethis(data))
        data_instance = json.loads(deletethis(data))
        InstanceName=data_instance['info']['name']
        AssetSources=data_instance['assetSources']
        if 'inst' in type(AssetSources[len(AssetSources)-1]):
            InstanceSave='instance'
        else:
            InstanceSave='default'
        if 'blacklist' in AssetSources[0]:
            direcList = directSearch(Config.SteamAppsPath + "\\workshop\content\\211820")
            blacklist = AssetSources[0]['blacklist']
            for i in range(len(blacklist)):
                if blacklist[i] in direcList:
                    direcList.remove(str(blacklist[i]))
            ListWorkshop = direcList
        else:
            for i in range(len(AssetSources)):
                try:
                    if type(AssetSources[i])==dict:
                        ModsID = AssetSources[i]['id']
                        print(ModsID)
                        ListWorkshop.append(int(ModsID))
                except:
                    return Translate.ErrorMultiboundModsID()
        init()
        config = cp.ConfigParser()
        config.read_file(open('config.ini'))

        config['INSTANCE' + str(Config.InstanceNumber + 1)] = {'Name': InstanceName, 'modslist': 'None',
                                                               'workshoplist': ListToString(ListWorkshop),'saveLocation':InstanceSave}
        Config.InstanceNumber = Config.InstanceNumber + 1
        with open('config.ini', 'w') as settings:
            config.write(settings)
        print(Translate.ChangeDone())
    return ChoiceWhatToDo()

def ConfigFile():
    init()
    try:
        choice = int(input(Translate.ConfigFile()))
    except:
        os.system("cls")
        return ConfigFile()
    if choice == 1:  # LanguageModif()
        try:
            choice = str(input(Translate.NewLanguage()))
        except:
            os.system("cls")
            return ConfigFile()
        config = cp.ConfigParser()
        config.read_file(open('config.ini'))
        if choice in ['fr', 'en']:
            config.set("OPTIONS", "language", choice)
            with open('config.ini', 'w') as settings:
                config.write(settings)
        os.system("cls")
        print(Translate.ChangeDone())
        return ConfigFile()
    elif choice == 2:  # ModeConfig()
        try:
            choice = int(input(Translate.ModeConfig()))
        except:
            os.system("cls")
            return ConfigFile()
        config = cp.ConfigParser()
        config.read_file(open('config.ini'))
        if choice in [1, 2, 3]:
            config.set("OPTIONS", "editormode", str(choice))
            with open('config.ini', 'w') as settings:
                config.write(settings)
        os.system("cls")
        print(Translate.ChangeDone())
        return ConfigFile()
    elif choice == 3:  # PathFinder()
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        if "starbound.exe" not in file_path.lower():
            return ConfigFile()
        else:
            file_path = file_path[:file_path.find("/common/")]
            config = cp.ConfigParser()
            config.read_file(open('config.ini'))
            config.set("OPTIONS", "steamappspath",
                       file_path)  # ('INSTANCE' + str(ch), 'WorkshopList', ListToString(WorkshopList))
            with open('config.ini', 'w') as settings:
                config.write(settings)
            os.system("cls")
            print(Translate.ChangeDone())
            return ConfigFile()
    elif choice == 4:  # unstableChoice
        print("WIP")  # todo unstable
        return ConfigFile()
    elif choice == 5:
        return ChoiceWhatToDo()
    else:
        return ConfigFile()


def refreshdic():
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
    return dic


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


def ChangeName(dic, ch):
    try:
        NewName = str(input(Translate.ChangeName(dic['Instance' + str(ch)][0])))
    except:
        return ChangeName(dic, ch)
    config = cp.ConfigParser()
    config.read_file(open('config.ini'))
    config.set('INSTANCE' + str(ch), 'Name', NewName)
    with open('config.ini', 'w') as settings:
        config.write(settings)
    os.system("cls")
    print(Translate.ChangeDone())
    return ModifyYourInstance(refreshdic(), ch)


def RemoveWorkshop(dic, ch, pgnb=0):
    InstanceLoad = dic['Instance' + str(ch)]
    WorkshopList = InstanceLoad[1].split(',')
    if Config.ShowMode == "2" or Config.ShowMode == "3":
        try:
            Changement = int(input(Translate.RemoveWorkshop2(dic['Instance' + str(ch)][1], pgnb)))
        except:
            os.system("cls")
            return RemoveWorkshop(dic, ch, pgnb)
    else:
        try:
            Changement = str(input(Translate.Workshop(dic['Instance' + str(ch)][1])))
        except:
            os.system("cls")
            return RemoveWorkshop(dic, ch)
    config = cp.ConfigParser()
    config.read_file(open('config.ini'))
    if Config.ShowMode == "2" or Config.ShowMode == "3":
        if Changement == 11:
            os.system("cls")
            return ModifyYourInstance(refreshdic(),ch)
        elif Changement == 12:
            if pgnb != 0:
                pgnb -= 1
            os.system("cls")
        elif Changement == 13:
            if ((pgnb + 1) * 10) < len(StringToList(dic['Instance' + str(ch)][1]))+len(StringToList(dic['Instance' + str(ch)][1]))%10:
                pgnb += 1
            print(((pgnb + 1) * 10) < len(StringToList(dic['Instance' + str(ch)][1]))+len(StringToList(dic['Instance' + str(ch)][1]))%10,pgnb)
            os.system("cls")
        elif 0 < Changement < 11:
            ListChangement = pageShow(pgnb, WorkshopList)[1]
            if ListChangement[Changement] in WorkshopList and ListChangement[Changement] != 10:
                WorkshopList.remove(ListChangement[Changement])
                if len(WorkshopList) == 0:
                    WorkshopList.append('None')
                config.set('INSTANCE' + str(ch), 'WorkshopList', ListToString(WorkshopList))
                with open('config.ini', 'w') as settings:
                    config.write(settings)
                os.system("cls")
                print(Translate.ChangeDone())
        return RemoveWorkshop(refreshdic(), ch, pgnb)
    else:
        if Changement == 0:
            config.set('INSTANCE' + str(ch), 'WorkshopList', 'None')
            with open('config.ini', 'w') as settings:
                config.write(settings)
            os.system("cls")
            print(Translate.ChangeDone())
            return ModifyYourInstance(refreshdic(), ch)
        elif Changement == 1:
            return ModifyYourInstance(refreshdic(), ch)
        elif str(Changement) not in WorkshopList:
            print(Translate.NotFound())
        else:
            for i in range(0, WorkshopList.count(str(Changement))):
                WorkshopList.remove(str(Changement))
            if len(WorkshopList) == 0:
                WorkshopList.append('None')
            config.set('INSTANCE' + str(ch), 'WorkshopList', ",".join(WorkshopList))
            with open('config.ini', 'w') as settings:
                config.write(settings)
            os.system("cls")
            print(Translate.ChangeDone())
            return RemoveWorkshop(refreshdic(), ch)


def RemoveMods(dic, ch, pgnb=0):
    InstanceLoad = dic['Instance' + str(ch)]
    ModsList = InstanceLoad[2].split(',')
    if Config.ShowMode == "2" or Config.ShowMode == "3":
        try:
            Changement = int(input(Translate.RemoveMods2(dic['Instance' + str(ch)][2], pgnb)))
        except:
            os.system("cls")
            return RemoveMods(dic, ch, pgnb)
    else:
        try:
            Changement = str(input(Translate.RemoveMods(dic['Instance' + str(ch)][2])))
        except:
            os.system("cls")
            return RemoveMods(dic, ch)
    config = cp.ConfigParser()
    config.read_file(open('config.ini'))
    if Config.ShowMode == "2" or Config.ShowMode == "3":
        if Changement == 11:
            os.system("cls")
            return ModifyYourInstance(refreshdic(), ch)
        elif Changement == 12:
            if pgnb != 0:
                pgnb -= 1
            os.system("cls")
        elif Changement == 13:
            if ((pgnb + 1) * 10) < len(StringToList(dic['Instance' + str(ch)][2]))+len(StringToList(dic['Instance' + str(ch)][2]))%10:
                pgnb += 1
            os.system("cls")
        elif 0 < Changement < 11:
            ListChangement = pageShow(pgnb, ModsList)[1]
            if ListChangement[Changement] in ModsList and ListChangement[Changement] != 10:
                ModsList.remove(ListChangement[Changement])
                if len(ModsList) == 0:
                    ModsList.append('None')
                config.set('INSTANCE' + str(ch), 'ModsList', ListToString(ModsList))
                with open('config.ini', 'w') as settings:
                    config.write(settings)
                os.system("cls")
                print(Translate.ChangeDone())
        return RemoveMods(refreshdic(), ch, pgnb)
    else:
        if Changement == '0':
            config.set('INSTANCE' + str(ch), 'ModsList', 'None')
            with open('config.ini', 'w') as settings:
                config.write(settings)
            print(Translate.ChangeDone())
            os.system("cls")
            return ModifyYourInstance(refreshdic(), ch)
        elif Changement == '1':
            os.system("cls")
            return ModifyYourInstance(refreshdic(), ch)
        elif str(Changement) not in ModsList:
            os.system("cls")
            print(Translate.NotFound())
        else:
            for i in range(0, ModsList.count(str(Changement))):
                ModsList.remove(str(Changement))
            if len(ModsList) == 0:
                ModsList.append('None')
            config.set('INSTANCE' + str(ch), 'ModsList', ",".join(ModsList))
            with open('config.ini', 'w') as settings:
                config.write(settings)
            os.system("cls")
            print(Translate.ChangeDone())
        return RemoveMods(refreshdic(), ch)


def AddMods(dic, ch, pgnb=0):
    InstanceLoad = dic['Instance' + str(ch)]
    modsList = InstanceLoad[2].split(',')
    direc = directSearch(Config.SteamAppsPath + "\common\\Starbound\mods") + pakSearch(Config.SteamAppsPath + "\common\\Starbound\mods")
    if Config.ShowMode == "2" or Config.ShowMode == "3":
        try:
            Changement = int(input(Translate.AddMods2(dic['Instance' + str(ch)][2], ",".join(direc), pgnb)))
        except:
            os.system("cls")
            return AddMods(dic, ch)
    else:
        try:
            Changement = str(input(Translate.AddMods(dic['Instance' + str(ch)][2], ",".join(direc))))
        except:
            os.system("cls")
            return AddMods(dic, ch)
    config = cp.ConfigParser()
    config.read_file(open('config.ini'))
    if Config.ShowMode == "2" or Config.ShowMode == "3":
        if Changement == 11:
            os.system("cls")
            return ModifyYourInstance(refreshdic(), ch)
        elif Changement == 12:
            if pgnb != 0:
                pgnb -= 1
            os.system("cls")
        elif Changement == 13:
            if ((pgnb + 1) * 10) < len(StringToList(",".join(direc).replace('.Disabled.', '')))+len(StringToList(",".join(direc).replace('.Disabled.', '')))%10:
                pgnb += 1
            os.system("cls")
        elif 0 < Changement < 11:
            ListChangement = pageShow(pgnb, StringToList(",".join(direc).replace('.Disabled.', '')))[1]
            if not ListChangement[Changement] in modsList and ListChangement[Changement] != 10:
                modsList.append(ListChangement[Changement])
                if 'None' in modsList:
                    modsList.remove('None')
                config.set('INSTANCE' + str(ch), 'ModsList', ListToString(modsList))
                with open('config.ini', 'w') as settings:
                    config.write(settings)
                os.system("cls")
                print(Translate.ChangeDone())
        return AddMods(refreshdic(), ch, pgnb)
    else:
        if Changement == '1':
            os.system("cls")
            return ModifyYourInstance(refreshdic(), ch)
        elif str(Changement) in modsList or (
                str(Changement) not in direc and '.Disabled.' + str(Changement) not in direc):
            os.system("cls")
        else:
            modsList.append(Changement)
            if 'None' in modsList:
                modsList.remove('None')
            config.set('INSTANCE' + str(ch), 'modsList', ListToString(modsList))
            os.system("cls")
            print(Translate.ChangeDone())
            with open('config.ini', 'w') as settings:
                config.write(settings)
        return AddMods(refreshdic(), ch)





def AddWorkshop(dic, ch, pgnb=0):
    InstanceLoad = dic['Instance' + str(ch)]
    WorkshopList = InstanceLoad[1].split(',')
    direc = directSearch(Config.SteamAppsPath + "\\workshop\content\\211820")
    if Config.ShowMode == "2" or Config.ShowMode == "3":
        try:
            Changement = int(input(Translate.WorkshopMod1(dic['Instance' + str(ch)][1], ",".join(direc), pgnb)))
        except:
            os.system("cls")
            return AddWorkshop(dic, ch, pgnb)
    else:
        try:
            Changement = int(input(Translate.AddWorkshop(dic['Instance' + str(ch)][1], ",".join(direc))))
        except:
            os.system("cls")
            return AddWorkshop(dic, ch)
    config = cp.ConfigParser()
    config.read_file(open('config.ini'))
    if Config.ShowMode == "2" or Config.ShowMode == "3":
        if Changement == 11:
            os.system("cls")
            return ModifyYourInstance(refreshdic(), ch)
        elif Changement == 12:
            if pgnb != 0:
                pgnb -= 1
            os.system("cls")
        elif Changement == 13:
            if ((pgnb + 1) * 10) < len(StringToList(",".join(direc).replace('.Disabled.', '')))+len(StringToList(",".join(direc).replace('.Disabled.', '')))%10:
                pgnb += 1
            os.system("cls")
        elif 0 < Changement < 11:
            ListChangement = pageShow(pgnb, StringToList(",".join(direc).replace('Disabled.', '')))[1]
            if not ListChangement[Changement] in WorkshopList and ListChangement[Changement] != 10:
                WorkshopList.append(ListChangement[Changement])
                if 'None' in WorkshopList:
                    WorkshopList.remove('None')
                config.set('INSTANCE' + str(ch), 'WorkshopList', ListToString(WorkshopList))
                os.system("cls")
                print(Translate.ChangeDone())
                with open('config.ini', 'w') as settings:
                    config.write(settings)
        return AddWorkshop(refreshdic(), ch, pgnb)
    else:
        if Changement == 1:
            os.system("cls")
            return ModifyYourInstance(refreshdic(), ch)
        elif str(Changement) in WorkshopList or (
                str(Changement) not in direc and 'Disabled.' + str(Changement) not in direc):
            os.system("cls")
        else:
            WorkshopList.append(Changement)
            if 'None' in WorkshopList:
                WorkshopList.remove('None')
            config.set('INSTANCE' + str(ch), 'WorkshopList', ListToString(WorkshopList))
            os.system("cls")
            print(Translate.ChangeDone())
            with open('config.ini', 'w') as settings:
                config.write(settings)
        return AddWorkshop(refreshdic(), ch)


def CollectionManipulate(dic, ch, Etat):
    if Etat:
        try:
            collectionid = int(input(Translate.Collection(Etat)))
        except:
            os.system("cls")
            return CollectionManipulate(dic, ch, Etat)
        InstanceLoad = dic['Instance' + str(ch)]
        WorkshopList = InstanceLoad[1].split(',')
        ListMods = Collection(collectionid)
        config = cp.ConfigParser()
        config.read_file(open('config.ini'))
        for i in range(len(ListMods)):
            if ListMods[i] not in WorkshopList:
                WorkshopList.append(ListMods[i])
        if 'None' in WorkshopList:
            WorkshopList.remove('None')
        config.set('INSTANCE' + str(ch), 'WorkshopList', ListToString(WorkshopList))
        os.system("cls")
        print(Translate.ChangeDone())
        with open('config.ini', 'w') as settings:
            config.write(settings)
    else:
        try:
            collectionid = int(input(Translate.Collection(Etat)))
        except:
            return CollectionManipulate(dic, ch, Etat)
        InstanceLoad = dic['Instance' + str(ch)]
        WorkshopList = InstanceLoad[1].split(',')
        ListMods = Collection(collectionid)
        config = cp.ConfigParser()
        config.read_file(open('config.ini'))
        for i in range(len(ListMods)):
            if ListMods[i] in WorkshopList:
                WorkshopList.remove(ListMods[i])
        if len(WorkshopList) == 0:
            WorkshopList.append('None')
        config.set('INSTANCE' + str(ch), 'WorkshopList', ListToString(WorkshopList))
        os.system("cls")
        print(Translate.ChangeDone())
        with open('config.ini', 'w') as settings:
            config.write(settings)
    return ModifyYourInstance(refreshdic(), ch)


def CleanerConfig():
    try:
        choice = int(input(Translate.Cleaner()))
    except:
        os.system("cls")
        return CleanerConfig()
    if choice == 1:
        dic = refreshdic()
        for i in range(1, Config.InstanceNumber + 1):
            WorkshopList = StringToList(dic['Instance' + str(i)][1])
            ModsList = StringToList(dic['Instance' + str(i)][2])
            direc = directSearch(Config.SteamAppsPath + "\\workshop\content\\211820")
            for y in range(len(direc)):
                direc[y] = direc[y].replace("Disabled.", "")
            y = 0
            while y < len(WorkshopList):
                temp = WorkshopList[y]
                if WorkshopList.count(temp) > 1 or (temp not in direc and temp!="None"):
                    y = 0
                else:
                    y = y + 1
                for w in range(0, 2):
                    if WorkshopList.count(temp) > 1:
                        while WorkshopList.count(temp) != 1:
                            WorkshopList.remove(temp)
                    if temp not in direc and temp != "None":
                        while WorkshopList.count(temp) != 0:
                            WorkshopList.remove(temp)
                    if len(WorkshopList) != 0:
                        temp = WorkshopList[len(WorkshopList) - 1]
            direc = directSearch(Config.SteamAppsPath + "\common\\Starbound\mods")
            for y in range(len(direc)):
                direc[y] = direc[y].replace(".Disabled.", "")
            y = 0
            while y < len(ModsList):
                temp = ModsList[y]
                if ModsList.count(temp) > 1 or (temp not in direc and temp!="None"):
                    y = 0
                else:
                    y = y + 1
                for w in range(0, 2):
                    if ModsList.count(temp) > 1:
                        while ModsList.count(temp) != 1:
                            ModsList.remove(temp)
                    if temp not in direc:
                        while ModsList.count(temp) != 0:
                            ModsList.remove(temp)
                    if len(ModsList) != 0:
                        temp = ModsList[len(ModsList) - 1]
            if len(ModsList) == 0:
                ModsList.append('None')
            if len(WorkshopList) == 0:
                WorkshopList.append('None')
            config = cp.ConfigParser()
            config.read_file(open('config.ini'))
            config.set('INSTANCE' + str(i), 'WorkshopList', ListToString(WorkshopList))
            config.set('INSTANCE' + str(i), 'modslist', ListToString(ModsList))
            with open('config.ini', 'w') as settings:
                config.write(settings)
        os.system("cls")
        print(Translate.ChangeDone())
    return ChoiceWhatToDo()


def ModifyYourInstance(dic, ch):
    InstanceLoad = dic['Instance' + str(ch)]
    try:
        choice = int(input(Translate.ModifyInstance(InstanceLoad)))
    except:
        os.system("cls")
        return ModifyYourInstance(dic, ch)
    if choice == 1:
        os.system("cls")
        return ChangeName(dic, ch)
    elif choice == 2:
        os.system("cls")
        return RemoveWorkshop(dic, ch)
    elif choice == 3:
        os.system("cls")
        return AddWorkshop(dic, ch)
    elif choice == 4:
        os.system("cls")
        return RemoveMods(dic, ch)
    elif choice == 5:
        os.system("cls")
        return AddMods(dic, ch)
    elif choice == 6:
        os.system("cls")
        return CollectionManipulate(dic, ch, True)
    elif choice == 7:
        os.system("cls")
        return CollectionManipulate(dic, ch, False)
    elif choice == 8:
        os.system("cls")
        return savelocation(dic,ch)
    elif choice == 9:
        os.system("cls")
        return ChooseYourInstance(dic)
    else:
        os.system("cls")
        return ModifyYourInstance(dic, ch)


def ChooseYourInstance(dic):
    try:
        for i in range(0, len(dic)):
            print(str(i + 1) + " " + dic['Instance' + str(i + 1)][0])
    except:
        return Translate.ErrorInstance()
    try:
        choice = int(input(Translate.ChooseInstance()))
    except :
        os.system("cls")
        return ChooseYourInstance(dic)
    if choice not in range(1, len(dic) + 1):
        os.system("cls")
        return ChooseYourInstance(dic)
    else:
        os.system("cls")
        return ModifyYourInstance(dic, choice)


print(init())
print(ChoiceWhatToDo())