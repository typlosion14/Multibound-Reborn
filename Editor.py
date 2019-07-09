from urllib.request import urlopen, Request
import configparser as cp
import os
from libCollectionSteam import Collection, TitleWorkshop
import tkinter as tk
from tkinter import filedialog


class Translate:
    def template(self=''):
        if Config.TranslateConfig == "fr":
            return
        else:
            return

    def ConfigFile(self=''):
        if Config.TranslateConfig == "fr":
            return "1.Changer la langue\n2.Changer le type d'affichage\n3.Changer le chemin de Starbound\n4.WIP\n5.Quitter\n"
        else:
            return "1.Change language\n2.Change how to display mods\n3.Change Starbound's path\n4.WIP\n5.Leave\n"

    def NewLanguage(self=''):
        if Config.TranslateConfig == "fr":
            return "Changer de Langue:'fr'=français,'en'=english\n"
        else:
            return "Change language:'fr'=français,'en'=english\n"

    def ModeConfig(self=''):
        if Config.TranslateConfig == "fr":
            return "Changer le type d'affichage:\n1.Vous devez rentrer le WorkshopID de l'item que vous souhaitez ajouter\n2.Système de page montrant les WorkshopID disponibles\n3.Système de page montrant les noms des mods(Prends plus de temps a charger)\n"
        else:
            return "Change how to display mods:\n1.You need to enter the WorkshopID of the mod you want to add\n2.Systeme of page show you the WorkshopID available\n3.Système of page show you the name of the mods(Take more time to load)\n"

    def Choice(self):
        if Config.TranslateConfig == "fr":
            return "Que voulez-vous faire?\n1.Modifier une instance\n2.En creez une nouvelle.\n3.Modifier le fichier config\n"
        else:
            return "What you want to do?\n1.Modify a existed Instance\n2.Create a new one.\n3.Modify the config file\n"

    def NameInstance(self=''):
        if Config.TranslateConfig == "fr":
            return "Choisissez le nom de l'instance:\n"
        else:
            return "Choose the instance's name:\n"

    def NotFound(self):
        if Config.TranslateConfig == "fr":
            return "Le fichier que vous avez selectione n'existe pas.\nVerifier bien que vous avez fini de telecharger le mods du workshop.\nOu si vous avez correctement taper le nom du mod.\n"
        else:
            return "File not found.\nPlease check if you have finish to download the mod on the workshop.\nOr if you have type correctly the name of the mod.\n"

    def UnstableBool(self):
        if Config.TranslateConfig == "fr":
            return 'Il y a un problème dans config.ini avec "Unstable"\nVeuillez entrer "False" ou "True".'
        else:
            return 'Problem in config.ini with "Unstable"\nPlease enter "False" or "True".'

    def SteamAppsPath(self):
        if Config.TranslateConfig == "fr":
            return "Il y a un problème dans config.ini avec 'SteamAppsPath'\nVeuillez verifier que le chemin amene bien vers workshop et common.\nSi cela ne fonctionne toujours place essayer 2\\ au lieu d'un seul."
        else:
            return "Problem in config.ini with 'SteamAppsPath'\nPlease check if in the path we have the repertories 'workshop' and 'common'.\nIf that's doesn't work try replace one \\ with two."

    def SuccessfulLoading(self):
        if Config.TranslateConfig == "fr":
            return "Chargement terminé avec succès!"
        else:
            return "Loading successfully completed!"

    def WhatYouWantToDo(self):
        if Config.TranslateConfig == "fr":
            return "Que voulez-vous faire?\n1.Modifier une instance\n2.En creez une nouvelle.\n"
        else:
            return "What you want to do?\n1.Modify Instance\n2.Create a new one\n"

    def ErrorInstance(self):
        if Config.TranslateConfig == "fr":
            return 'Il y a un problème dans config.ini lié aux instances.\nVerifié si vos instances sont crées avec la forme: \n[INSTANCE1]\nWorshopList = 211,277\nModsList=None\nAussi si vous ne voulez pas charger de mods,écrivez "None" au lieu de rien.'
        else:
            return "Problem in config.ini link with instance.\nCheck if instance are created in this form: \n[INSTANCE1]\nWorshopList = 211,277\nModsList=None\nAlso if you don't want to load mod write 'None' and not nothing."

    def ChooseInstance(self):
        if Config.TranslateConfig == "fr":
            return "Choissisez l'instance que vous souhaitez Modifier:"
        else:
            return "Choose instance you want to modify:"

    def ChangeName(name):
        if Config.TranslateConfig == "fr":
            return "Le nom actuel est " + name + "\nQuel est son nouveau nom?\n"
        else:
            return "Actuel name is " + name + "\nWhat is it new name?\n"

    def ChangeDone(self):
        if Config.TranslateConfig == "fr":
            return "Changement effectué."
        else:
            return "Change done."

    def Collection(Etat):
        if Etat:
            if Config.TranslateConfig == "fr":
                return "Quel collection voulez-vous ajouter (Attention tous les mods seront ajoutés):\n"
            else:
                return "What collection you want to add (Be careful all mods will be added):\n"
        else:
            if Config.TranslateConfig == "fr":
                return "Quel collection voulez-vous retirer (Attetion tous les mods seront retirés):\n"
            else:
                return "What collection you want to delete (Be careful all mods will be retrieved):\n"

    def AddMods(WorkshopList, direc):  # Add Mods Config 1
        if Config.TranslateConfig == "fr":
            return "Voici les mods de la liste:" + WorkshopList + "\nVoici les mods installés:" + direc + "\nQuel mod voulez-vous rajoutez (ecrivez '1' pour quitter)?\n"
        else:
            return "Here the mods list:" + WorkshopList + "\nHere the installed mods:" + direc + "\nWhat mod you want to add (write '1' for leave)?\n"

    def RemoveMods(modsList):  # Remove Mods Config 1
        if Config.TranslateConfig == "fr":
            return "Voici les mods :" + modsList + "\nQuel mod voulez-vous enlevez (ecrivez '0' pour tous et '1' pour quitter)?\n"
        else:
            return "Here the mods:" + modsList + "\nWhat mod you want to remove (write '0' for all and '1' for leave)?\n"

    def RemoveWorkshop2(modsList, pgnb):  # Delete Workshop Config 2
        if Config.TranslateConfig == "fr":
            return "Quel Objet voulez-vous enlevez ?\n" + pageShow(pgnb, convertString(modsList))[
                0] + "11.Quitter\n12.Page Précédente\n13.Page Suivante\n"
        else:
            return "What object you want to remove ?\n" + pageShow(pgnb, convertString(modsList))[
                0] + "11.Leave\n12.Previous Page\n13.Next Page\n"

    def RemoveMods2(modsList, pgnb):  # Remove Mods Config 2
        if Config.TranslateConfig == "fr":
            return "Quel mod voulez-vous enlevez ?\n" + pageShow(pgnb, convertString(modsList))[
                0] + "11.Quitter\n12.Page Précédente\n13.Page Suivante\n"
        else:
            return "What mod you want to remove ?\n" + pageShow(pgnb, convertString(modsList))[
                0] + "11.Leave\n12.Previous Page\n13.Next Page\n"

    def WorkshopMod1(WorkshopList, direc, pgnb):  # Add Workshop Config 2
        if Config.TranslateConfig == "fr":
            return "Voici les objets du Workshop:" + WorkshopList + "\nQuel Objet voulez-vous rajoutez ?\n" + \
                   pageShow(pgnb, convertString(direc.replace('Disabled.', '')))[
                       0] + "11.Quitter\n12.Page Précédente\n13.Page Suivante\n"
        else:
            return "Here the workshop object:" + WorkshopList + "\nWhat object you want to add ?\n" + \
                   pageShow(pgnb, convertString(direc.replace('Disabled.', '')))[
                       0] + "11.Leave\n12.Previous Page\n13.Next Page\n"

    def AddMods2(WorkshopList, direc, pgnb):  # Add Mods Config 2
        if Config.TranslateConfig == "fr":
            return "Voici les mods de la liste:" + WorkshopList + "\nQuel mod voulez-vous rajoutez ?\n" + \
                   pageShow(pgnb, convertString(direc.replace('.Disabled.', '')))[
                       0] + "11.Quitter\n12.Page Précédente\n13.Page Suivante\n"
        else:
            return "Here the mods list:" + WorkshopList + "\nWhat mod you want to add ?\n" + \
                   pageShow(pgnb, convertString(direc.replace('.Disabled.', '')))[
                       0] + "11.Leave\n12.Previous Page\n13.Next Page\n"

    def AddWorkshop(WorkshopList, direc):  # Add Workshop Config 1
        if Config.TranslateConfig == "fr":
            return "Voici les objets du Workshop:" + WorkshopList + "\nVoici les objets installés:" + direc.replace(
                'Disabled.', '') + "\nQuel Objet voulez-vous rajoutez (ecrivez '1' pour quitter)?\n"
        else:
            return "Here the workshop object:" + WorkshopList + "\nHere the installed object:" + direc.replace(
                'Disabled.', '') + "\nWhat object you want to add (write '1' for leave)?\n"

    def Workshop(WorkshopList):  # Delete Workshop Config 1
        if Config.TranslateConfig == "fr":
            return "Voici les objets du Workshop:" + WorkshopList + "\nQuel Objet voulez-vous enlevez (ecrivez '0' pour tous et '1' pour quitter)?\n"
        else:
            return "Here the workshop object:" + WorkshopList + "\nWhat object you want to remove (write '0' for all and '1' for leave)?\n"

    def ModifyInstance(InstanceLoad):
        InstanceName = str(InstanceLoad[0])
        Workshop = InstanceLoad[1]
        ModLoad = InstanceLoad[2]
        if Config.TranslateConfig == "fr":
            return "Vous avez chargez l'instance:" + InstanceName + "\nLes mods du Workshop sont " + Workshop + "\nLes mods sont " + ModLoad.replace(
                'Disabled.',
                '') + "\nQue voulez-vous faire?\n1.Renommer l'instance\n2.Supprimez un mod de la liste du Workshop\n3.Rajouter un mod à la liste du Workshop\n4.Supprimez un mod de la liste des mods\n5.Rajouter un mod à la liste des Mods\n6.Rajouter une collection\n7.Supprimer une collection\n8.Changez d'instance\n"
        else:
            return "You have load:" + InstanceName + "\nWorkshop list: " + Workshop + "\nMods list :" + ModLoad.replace(
                'Disabled.',
                '') + "\nWhat you want to do?\n1.Rename Instance\n2.Delete a mod in Workshop List\n3.Add a mod in Workshop List\n4.Delete a mod in Mods List\n5.Add a mod in Mods List\n6.Add a collection\n7.Delete a collection\n8.Change the selected Instance\n"


class Config:
    TranslateConfig = "en"
    Unstable = False
    InstanceNumber = 1
    SteamAppsPath = "D:\SteamLibrary\steamapps"
    OriginPath = ".\\"
    ShowMode = "1"


def pageShow(pgnb, modsList):
    print(modsList)
    msg = ''
    List = [10] * 11
    if modsList[0] != 'None':
        if (10 * pgnb + 10) <= len(modsList):
            for i in range(0, 10):
                if Config.ShowMode == "2":
                    msg = msg + str(i + 1) + '.' + modsList[(10 * pgnb) + i] + '\n'
                elif Config.ShowMode == "3":
                    msg = msg + str(i + 1) + '.' + TitleWorkshop(modsList[(10 * pgnb) + i]) + '\n'
                List[i + 1] = modsList[(10 * pgnb) + i]
        else:
            if 10 * pgnb > len(modsList):
                pgnb = len(modsList) % 10
            for i in range(0, len(modsList) % 10):
                if Config.ShowMode == "2":
                    msg = msg + str(i + 1) + '.' + modsList[(10 * pgnb) + i] + '\n'
                elif Config.ShowMode == "3":
                    msg = msg + str(i + 1) + '.' + TitleWorkshop(modsList[(10 * pgnb) + i]) + '\n'
                List[i + 1] = modsList[(10 * pgnb) + i]
    else:
        msg = "None\n"
        List = ['None'] * 11
    return msg, List


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


def init():
    config = cp.ConfigParser()
    config.read_file(open('config.ini'))
    Config.OriginPath = os.getcwd()
    Config.InstanceNumber = int(len(config.sections()[1:]))
    Config.ShowMode = str(config.get('OPTIONS', 'editormode'))
    try:
        Config.Unstable = bool(config.get('OPTIONS', 'Unstable'))
    except:
        return Translate.UnstableBool("")
    if config.get('OPTIONS', 'Language') != "en" and config.get('OPTIONS', 'Language') in ("fr"):
        Config.TranslateConfig = config.get('OPTIONS', 'Language')
    try:
        SteamAppsPath = config.get('OPTIONS', 'SteamAppsPath')
        os.chdir(SteamAppsPath + "\\workshop\content\\211820")
        os.chdir(SteamAppsPath + "\\common\Starbound")  # Unstable change todo
        os.chdir(SteamAppsPath)
        Config.SteamAppsPath = SteamAppsPath
        os.chdir(Config.OriginPath)
    except:
        return Translate.SteamAppsPath("")
    return Translate.SuccessfulLoading("")


def CreateInstance():
    NameInstance = str(input(Translate.NameInstance('')))
    if NameInstance == '' or NameInstance == 'None':
        NameInstance = 'NewInstance'
    config = cp.ConfigParser()
    config.read_file(open('config.ini'))
    config['INSTANCE' + str(Config.InstanceNumber + 1)] = {'Name': NameInstance, 'modslist': 'None',
                                                           'workshoplist': 'None'}
    Config.InstanceNumber = Config.InstanceNumber + 1
    with open('config.ini', 'w') as settings:
        config.write(settings)
    return ChooseYourInstance(refreshdic())


def ChoiceWhatToDo():
    try:
        ch = int(input(Translate.Choice('')))
    except:
        return ChoiceWhatToDo()
    if ch == 1:
        return LoadingInstance()
    elif ch == 2:
        return CreateInstance()
    elif ch == 3:
        return ConfigFile()
    else:
        return ChoiceWhatToDo()


def ConfigFile():
    init()
    try:
        choice = int(input(Translate.ConfigFile('')))
    except:
        return ConfigFile()
    if choice == 1:  # LanguageModif()
        try:
            choice = str(input(Translate.NewLanguage('')))
        except:
            return ConfigFile()
        print(choice)
        config = cp.ConfigParser()
        config.read_file(open('config.ini'))
        if choice in ['fr', 'en']:
            config.set("OPTIONS", "language", choice)
            with open('config.ini', 'w') as settings:
                config.write(settings)
        return ConfigFile()
    if choice == 2:  # ModeConfig()
        try:
            choice = int(input(Translate.ModeConfig('')))
        except:
            return ConfigFile()
        print(choice)
        config = cp.ConfigParser()
        config.read_file(open('config.ini'))
        if choice in [1, 2, 3]:
            config.set("OPTIONS", "editormode", str(choice))
            with open('config.ini', 'w') as settings:
                config.write(settings)
        return ConfigFile()
    if choice == 3:  # PathFinder()
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        print(file_path)
        if "starbound.exe" not in file_path.lower():
            return ConfigFile()
        else:
            file_path = file_path[:file_path.find("/common/")]
            config = cp.ConfigParser()
            config.read_file(open('config.ini'))
            config.set("OPTIONS", "steamappspath",
                       file_path)  # ('INSTANCE' + str(ch), 'WorkshopList', convertList(WorkshopList))
            with open('config.ini', 'w') as settings:
                config.write(settings)
            print(Translate.ChangeDone(""))
            return ConfigFile()
    if choice == 4:  # unstableChoice
        print("WIP")  # todo unstable
        return ConfigFile()
    if choice == 5:
        return ChoiceWhatToDo()
    else:
        ConfigFile()


def refreshdic():
    config = cp.ConfigParser()
    config.read_file(open('config.ini'))
    dic = {}
    try:
        for i in range(0, Config.InstanceNumber):
            dic['Instance' + str(i + 1)] = config.get('INSTANCE' + str(i + 1), 'Name'), config.get(
                'INSTANCE' + str(i + 1), 'workshoplist'), config.get('INSTANCE' + str(i + 1), 'ModsList')
    except:
        return Translate.ErrorInstance('')
    return dic


def LoadingInstance():
    config = cp.ConfigParser()
    config.read_file(open('config.ini'))
    dic = {}
    try:
        for i in range(0, Config.InstanceNumber):
            dic['Instance' + str(i + 1)] = config.get('INSTANCE' + str(i + 1), 'Name'), config.get(
                'INSTANCE' + str(i + 1), 'workshoplist'), config.get('INSTANCE' + str(i + 1), 'ModsList')
    except:
        return Translate.ErrorInstance('')
    return ChooseYourInstance(dic)


def ChangeName(dic, ch):
    try:
        NewName = str(input(Translate.ChangeName(dic['Instance' + str(ch)][0])))
    except:
        ChangeName(dic, ch)
    config = cp.ConfigParser()
    config.read_file(open('config.ini'))
    config.set('INSTANCE' + str(ch), 'Name', NewName)
    with open('config.ini', 'w') as settings:
        config.write(settings)
    print(Translate.ChangeDone(''))
    return ModifyYourInstance(refreshdic(), ch)


def RemoveWorkshop(dic, ch, pgnb=0):
    InstanceLoad = dic['Instance' + str(ch)]
    WorkshopList = InstanceLoad[1].split(',')
    if Config.ShowMode == "2" or Config.ShowMode == "3":
        try:
            Changement = int(input(Translate.RemoveWorkshop2(dic['Instance' + str(ch)][1], pgnb)))
        except:
            return RemoveWorkshop(dic, ch, pgnb)
    else:
        try:
            Changement = str(input(Translate.Workshop(dic['Instance' + str(ch)][1])))
        except:
            return RemoveWorkshop(dic, ch)
    config = cp.ConfigParser()
    config.read_file(open('config.ini'))
    if Config.ShowMode == "2" or Config.ShowMode == "3":
        if Changement == 11:
            return ModifyYourInstance(refreshdic(), ch)
        elif Changement == 12:
            if pgnb != 0:
                pgnb -= 1
            return RemoveWorkshop(refreshdic(), ch, pgnb)
        elif Changement == 13:
            if ((pgnb + 1) * 10) < len(convertString(dic['Instance' + str(ch)][1])):
                pgnb += 1
                return RemoveWorkshop(refreshdic(), ch, pgnb)
            else:
                return RemoveWorkshop(refreshdic(), ch, pgnb)
        elif 0 < Changement < 11:
            ListChangement = pageShow(pgnb, WorkshopList)[1]
            print(ListChangement, ListChangement[Changement])
            if ListChangement[Changement] in WorkshopList and ListChangement[Changement] != 10:
                WorkshopList.remove(ListChangement[Changement])
                print(ListChangement[Changement])
                if len(WorkshopList) == 0:
                    WorkshopList.append('None')
                config.set('INSTANCE' + str(ch), 'WorkshopList', convertList(WorkshopList))
                print(convertList(WorkshopList))
                print(Translate.ChangeDone(''))
                with open('config.ini', 'w') as settings:
                    config.write(settings)
                return RemoveWorkshop(refreshdic(), ch, pgnb)
            else:
                return RemoveWorkshop(refreshdic(), ch, pgnb)
    else:
        if Changement == 0:
            config.set('INSTANCE' + str(ch), 'WorkshopList', 'None')
            with open('config.ini', 'w') as settings:
                config.write(settings)
            print(Translate.ChangeDone(''))
            return ModifyYourInstance(refreshdic(), ch)
        elif Changement == 1:
            return ModifyYourInstance(refreshdic(), ch)
        elif str(Changement) not in WorkshopList:
            print(Translate.NotFound(''))
        else:
            for i in range(0, WorkshopList.count(str(Changement))):
                WorkshopList.remove(str(Changement))
            if len(WorkshopList) == 0:
                WorkshopList.append('None')
            config.set('INSTANCE' + str(ch), 'WorkshopList', ",".join(WorkshopList))
            with open('config.ini', 'w') as settings:
                config.write(settings)
            print(Translate.ChangeDone(''))
            return RemoveWorkshop(refreshdic(), ch)


def RemoveMods(dic, ch, pgnb=0):
    InstanceLoad = dic['Instance' + str(ch)]
    ModsList = InstanceLoad[2].split(',')
    if Config.ShowMode == "2" or Config.ShowMode == "3":
        try:
            Changement = int(input(Translate.RemoveMods2(dic['Instance' + str(ch)][2], pgnb)))
        except:
            return RemoveMods(dic, ch, pgnb)
    else:
        try:
            Changement = str(input(Translate.RemoveMods(dic['Instance' + str(ch)][2])))
        except:
            return RemoveMods(dic, ch)
    config = cp.ConfigParser()
    config.read_file(open('config.ini'))
    if Config.ShowMode == "2" or Config.ShowMode == "3":
        if Changement == 11:
            return ModifyYourInstance(refreshdic(), ch)
        elif Changement == 12:
            if pgnb != 0:
                pgnb -= 1
            return RemoveMods(refreshdic(), ch, pgnb)
        elif Changement == 13:
            if ((pgnb + 1) * 10) < len(convertString(dic['Instance' + str(ch)][2])):
                pgnb += 1
                return RemoveMods(refreshdic(), ch, pgnb)
            else:
                return RemoveMods(refreshdic(), ch, pgnb)
        elif 0 < Changement < 11:
            ListChangement = pageShow(pgnb, ModsList)[1]
            if ListChangement[Changement] in ModsList and ListChangement[Changement] != 10:
                ModsList.remove(ListChangement[Changement])
                print(ModsList, convertList(ModsList))
                if len(ModsList) == 0:
                    ModsList.append('None')
                config.set('INSTANCE' + str(ch), 'ModsList', convertList(ModsList))
                print(Translate.ChangeDone(''))
                with open('config.ini', 'w') as settings:
                    config.write(settings)
                return RemoveMods(refreshdic(), ch, pgnb)
            else:
                return RemoveMods(refreshdic(), ch, pgnb)
        else:
            return RemoveMods(dic, ch, pgnb)
    else:
        if Changement == '0':
            config.set('INSTANCE' + str(ch), 'ModsList', 'None')
            with open('config.ini', 'w') as settings:
                config.write(settings)
            print(Translate.ChangeDone(''))
            return ModifyYourInstance(refreshdic(), ch)
        elif Changement == '1':
            return ModifyYourInstance(refreshdic(), ch)
        elif str(Changement) not in ModsList:
            print(Translate.NotFound(''))
            return RemoveMods(refreshdic(), ch, pgnb)
        else:
            for i in range(0, ModsList.count(str(Changement))):
                ModsList.remove(str(Changement))
            if len(ModsList) == 0:
                ModsList.append('None')
            config.set('INSTANCE' + str(ch), 'ModsList', ",".join(ModsList))
            with open('config.ini', 'w') as settings:
                config.write(settings)
            print(Translate.ChangeDone(''))
            return RemoveMods(refreshdic(), ch)


def AddMods(dic, ch, pgnb=0):
    InstanceLoad = dic['Instance' + str(ch)]
    modsList = InstanceLoad[2].split(',')
    direc = directSearch(Config.SteamAppsPath + "\common\\Starbound\mods")
    if Config.ShowMode == "2" or Config.ShowMode == "3":
        try:
            Changement = int(input(Translate.AddMods2(dic['Instance' + str(ch)][2], ",".join(direc), pgnb)))
        except:
            return AddMods(dic, ch)
    else:
        try:
            Changement = str(input(Translate.AddMods(dic['Instance' + str(ch)][2], ",".join(direc))))
        except:
            return AddMods(dic, ch)
    config = cp.ConfigParser()
    config.read_file(open('config.ini'))
    if Config.ShowMode == "2" or Config.ShowMode == "3":
        if Changement == 11:
            return ModifyYourInstance(refreshdic(), ch)
        elif Changement == 12:
            if pgnb != 0:
                pgnb -= 1
            return AddMods(refreshdic(), ch, pgnb)
        elif Changement == 13:
            if ((pgnb + 1) * 10) < len(convertString(dic['Instance' + str(ch)][2])):
                pgnb += 1
            return AddMods(refreshdic(), ch, pgnb)
        elif 0 < Changement < 11:
            ListChangement = pageShow(pgnb, convertString(",".join(direc).replace('.Disabled.', '')))[1]
            if not ListChangement[Changement] in modsList and ListChangement[Changement] != 10:
                modsList.append(ListChangement[Changement])
                if 'None' in modsList:
                    modsList.remove('None')
                config.set('INSTANCE' + str(ch), 'ModsList', convertList(modsList))
                print(Translate.ChangeDone(''))
                with open('config.ini', 'w') as settings:
                    config.write(settings)
                return AddMods(refreshdic(), ch, pgnb)
            else:
                return AddMods(refreshdic(), ch, pgnb)
        else:
            return AddMods(dic, ch, pgnb)
    else:
        if Changement == '1':
            return ModifyYourInstance(refreshdic(), ch)
        elif str(Changement) in modsList or (
                str(Changement) not in direc and '.Disabled.' + str(Changement) not in direc):
            return AddMods(refreshdic(), ch)
        else:
            modsList.append(Changement)
            if 'None' in modsList:
                modsList.remove('None')
            config.set('INSTANCE' + str(ch), 'modsList', convertList(modsList))
            print(Translate.ChangeDone(''))
            with open('config.ini', 'w') as settings:
                config.write(settings)
            return AddMods(refreshdic(), ch)


def directSearch(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]


def convertList(list):
    string = ''
    for i in range(len(list)):
        if i != len(list) - 1:
            string = string + str(list[i]) + ','
        else:
            string = string + str(list[i])
    return string


def convertString(string):
    # print(string)
    list = []
    pos1 = 0
    for i in range(string.count(",")):
        list.append(string[pos1:string.index(",", pos1)])
        pos1 = string.index(",", pos1) + 1
    list.append(string[pos1:])
    # print(list)
    return list


def AddWorkshop(dic, ch, pgnb=0):
    InstanceLoad = dic['Instance' + str(ch)]
    WorkshopList = InstanceLoad[1].split(',')
    direc = directSearch(Config.SteamAppsPath + "\\workshop\content\\211820")
    if Config.ShowMode == "2" or Config.ShowMode == "3":
        try:
            print(dic['Instance' + str(ch)][1])
            Changement = int(input(Translate.WorkshopMod1(dic['Instance' + str(ch)][1], ",".join(direc), pgnb)))
        except:
            print("ERROR")
            return AddWorkshop(dic, ch, pgnb)
    else:
        try:
            Changement = int(input(Translate.AddWorkshop(dic['Instance' + str(ch)][1], ",".join(direc))))
        except:
            return AddWorkshop(dic, ch)
    config = cp.ConfigParser()
    config.read_file(open('config.ini'))
    if Config.ShowMode == "2" or Config.ShowMode == "3":
        if Changement == 11:
            return ModifyYourInstance(refreshdic(), ch)
        elif Changement == 12:
            if pgnb != 0:
                pgnb -= 1
            return AddWorkshop(refreshdic(), ch, pgnb)
        elif Changement == 13:
            print("ALED", pgnb, convertString(",".join(direc)))
            if ((pgnb + 1) * 10) < len(convertString(",".join(direc))):
                pgnb += 1
            return AddWorkshop(refreshdic(), ch, pgnb)
        elif 0 < Changement < 11:
            ListChangement = pageShow(pgnb, convertString(",".join(direc).replace('Disabled.', '')))[1]
            if not ListChangement[Changement] in WorkshopList and ListChangement[Changement] != 10:
                WorkshopList.append(ListChangement[Changement])
                if 'None' in WorkshopList:
                    WorkshopList.remove('None')
                config.set('INSTANCE' + str(ch), 'WorkshopList', convertList(WorkshopList))
                print(Translate.ChangeDone(''))
                with open('config.ini', 'w') as settings:
                    config.write(settings)
                return AddWorkshop(refreshdic(), ch, pgnb)
            else:
                return AddWorkshop(refreshdic(), ch, pgnb)
        else:
            return AddWorkshop(dic, ch, pgnb)
    else:
        if Changement == 1:
            return ModifyYourInstance(refreshdic(), ch)
        elif str(Changement) in WorkshopList or (
                str(Changement) not in direc and 'Disabled.' + str(Changement) not in direc):
            return AddWorkshop(refreshdic(), ch)
        else:
            WorkshopList.append(Changement)
            if 'None' in WorkshopList:
                WorkshopList.remove('None')
            config.set('INSTANCE' + str(ch), 'WorkshopList', convertList(WorkshopList))
            print(Translate.ChangeDone(''))
            with open('config.ini', 'w') as settings:
                config.write(settings)
            return AddWorkshop(refreshdic(), ch)


def CollectionManipulate(dic, ch, Etat):
    if Etat:
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
            if ListMods[i] not in WorkshopList:
                WorkshopList.append(ListMods[i])
        if 'None' in WorkshopList:
            WorkshopList.remove('None')
        config.set('INSTANCE' + str(ch), 'WorkshopList', convertList(WorkshopList))
        print(Translate.ChangeDone(''))
        with open('config.ini', 'w') as settings:
            config.write(settings)
        return ModifyYourInstance(refreshdic(), ch)
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
        config.set('INSTANCE' + str(ch), 'WorkshopList', convertList(WorkshopList))
        print(Translate.ChangeDone(''))
        with open('config.ini', 'w') as settings:
            config.write(settings)
        return ModifyYourInstance(refreshdic(), ch)


def ModifyYourInstance(dic, ch):
    InstanceLoad = dic['Instance' + str(ch)]
    try:
        choice = int(input(Translate.ModifyInstance(InstanceLoad)))
    except:
        return ModifyYourInstance(dic, ch)
    if choice == 1:
        return ChangeName(dic, ch)
    elif choice == 2:
        return RemoveWorkshop(dic, ch)
    elif choice == 3:
        return AddWorkshop(dic, ch)
    elif choice == 4:
        return RemoveMods(dic, ch)
    elif choice == 5:
        return AddMods(dic, ch)
    elif choice == 6:
        return CollectionManipulate(dic, ch, True)
    elif choice == 7:
        return CollectionManipulate(dic, ch, False)
    elif choice == 8:
        return ChooseYourInstance(dic)
    else:
        return ModifyYourInstance(dic, ch)


def ChooseYourInstance(dic):
    try:
        for i in range(0, len(dic)):
            print(str(i + 1) + " " + dic['Instance' + str(i + 1)][0])
    except:
        return Translate.ErrorInstance("")
    try:
        choice = int(input(Translate.ChooseInstance("")))
    except:
        return ChooseYourInstance(dic)
    if choice not in range(1, len(dic) + 1):
        return ChooseYourInstance(dic)
    else:
        return ModifyYourInstance(dic, choice)


print(init())
print(ChoiceWhatToDo())
