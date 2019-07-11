import configparser as cp
import os

from CobraLib import StringToList
from libCollectionSteam import TitleWorkshop


class Translate:
    def template(self=''):
        if Config.TranslateConfig == "fr":
            return
        else:
            return

    def Cleaner(self=''):
        if Config.TranslateConfig == "fr":
            return "Voulez-vous nettoyer le fichier config ?\n1.Oui\n2.Non\n"
        else:
            return "Do you want to clean the config file?\n1.Oui\n2.None\n"

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

    def Choice(self=''):
        if Config.TranslateConfig == "fr":
            return "Que voulez-vous faire?\n1.Modifier une instance\n2.En creez une nouvelle.\n3.Modifier le fichier config\n4.Nettoyez le fichier config\n"
        else:
            return "What you want to do?\n1.Modify a existed Instance\n2.Create a new one.\n3.Modify the config file\n4.Clean the config file\n"

    def NameInstance(self=''):
        if Config.TranslateConfig == "fr":
            return "Choisissez le nom de l'instance:\n"
        else:
            return "Choose the instance's name:\n"

    def NotFound(self=''):
        if Config.TranslateConfig == "fr":
            return "Le fichier que vous avez selectione n'existe pas.\nVerifier bien que vous avez fini de telecharger le mods du workshop.\nOu si vous avez correctement taper le nom du mod.\n"
        else:
            return "File not found.\nPlease check if you have finish to download the mod on the workshop.\nOr if you have type correctly the name of the mod.\n"

    def UnstableBool(self=''):
        if Config.TranslateConfig == "fr":
            return 'Il y a un problème dans config.ini avec "Unstable"\nVeuillez entrer "False" ou "True".'
        else:
            return 'Problem in config.ini with "Unstable"\nPlease enter "False" or "True".'

    def SteamAppsPath(self=''):
        if Config.TranslateConfig == "fr":
            return "Il y a un problème dans config.ini avec 'SteamAppsPath'\nVeuillez verifier que le chemin amene bien vers workshop et common.\nSi cela ne fonctionne toujours place essayer 2\\ au lieu d'un seul."
        else:
            return "Problem in config.ini with 'SteamAppsPath'\nPlease check if in the path we have the repertories 'workshop' and 'common'.\nIf that's doesn't work try replace one \\ with two."

    def SuccessfulLoading(self=''):
        if Config.TranslateConfig == "fr":
            return "Chargement terminé avec succès!"
        else:
            return "Loading successfully completed!"

    def WhatYouWantToDo(self=''):
        if Config.TranslateConfig == "fr":
            return "Que voulez-vous faire?\n1.Modifier une instance\n2.En creez une nouvelle.\n"
        else:
            return "What you want to do?\n1.Modify Instance\n2.Create a new one\n"

    def ErrorInstance(self=''):
        if Config.TranslateConfig == "fr":
            return 'Il y a un problème dans config.ini lié aux instances.\nVerifié si vos instances sont crées avec la forme: \n[INSTANCE1]\nWorshopList = 211,277\nModsList=None\nAussi si vous ne voulez pas charger de mods,écrivez "None" au lieu de rien.'
        else:
            return "Problem in config.ini link with instance.\nCheck if instance are created in this form: \n[INSTANCE1]\nWorshopList = 211,277\nModsList=None\nAlso if you don't want to load mod write 'None' and not nothing."

    def ChooseInstance(self=''):
        if Config.TranslateConfig == "fr":
            return "Choissisez l'instance que vous souhaitez Modifier:"
        else:
            return "Choose instance you want to modify:"

    def ChangeName(name):
        if Config.TranslateConfig == "fr":
            return "Le nom actuel est " + name + "\nQuel est son nouveau nom?\n"
        else:
            return "Actuel name is " + name + "\nWhat is it new name?\n"

    def ChangeDone(self=''):
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
            return "Quel Objet voulez-vous enlevez ?\n" + pageShow(pgnb, StringToList(modsList))[
                0] + "11.Quitter\n12.Page Précédente\n13.Page Suivante\n"
        else:
            return "What object you want to remove ?\n" + pageShow(pgnb, StringToList(modsList))[
                0] + "11.Leave\n12.Previous Page\n13.Next Page\n"

    def RemoveMods2(modsList, pgnb):  # Remove Mods Config 2
        if Config.TranslateConfig == "fr":
            return "Quel mod voulez-vous enlevez ?\n" + pageShow(pgnb, StringToList(modsList))[
                0] + "11.Quitter\n12.Page Précédente\n13.Page Suivante\n"
        else:
            return "What mod you want to remove ?\n" + pageShow(pgnb, StringToList(modsList))[
                0] + "11.Leave\n12.Previous Page\n13.Next Page\n"

    def WorkshopMod1(WorkshopList, direc, pgnb):  # Add Workshop Config 2
        if Config.TranslateConfig == "fr":
            return "Voici les objets du Workshop:" + WorkshopList + "\nQuel Objet voulez-vous rajoutez ?\n" + \
                   pageShow(pgnb, StringToList(direc.replace('Disabled.', '')))[
                       0] + "11.Quitter\n12.Page Précédente\n13.Page Suivante\n"
        else:
            return "Here the workshop object:" + WorkshopList + "\nWhat object you want to add ?\n" + \
                   pageShow(pgnb, StringToList(direc.replace('Disabled.', '')))[
                       0] + "11.Leave\n12.Previous Page\n13.Next Page\n"

    def AddMods2(WorkshopList, direc, pgnb):  # Add Mods Config 2
        if Config.TranslateConfig == "fr":
            return "Voici les mods de la liste:" + WorkshopList + "\nQuel mod voulez-vous rajoutez ?\n" + \
                   pageShow(pgnb, StringToList(direc.replace('.Disabled.', '')))[
                       0] + "11.Quitter\n12.Page Précédente\n13.Page Suivante\n"
        else:
            return "Here the mods list:" + WorkshopList + "\nWhat mod you want to add ?\n" + \
                   pageShow(pgnb, StringToList(direc.replace('.Disabled.', '')))[
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

    def ModifyInstance(InstanceLoad=''):
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

    # ^^^^^^^^Editor
    #               Mainvvvvvvvv
    def loading(self=''):
        if Config.TranslateConfig == "fr":
            return "Chargement de votre Instance..."
        else:
            return "Loading of your instance..."

    def ChooseInstance(self=''):
        if Config.TranslateConfig == "fr":
            return "Choissisez l'instance que vous souhaitez:"
        else:
            return "Choose your instance:"

    def UnstableBool(self=''):
        if Config.TranslateConfig == "fr":
            return 'Il y a un problème dans config.ini avec "Unstable"\nVeuillez entrer "False" ou "True".'
        else:
            return 'Problem in config.ini with "Unstable"\nPlease enter "False" or "True".'

    def SteamAppsPath(self=''):
        if Config.TranslateConfig == "fr":
            return "Il y a un problème dans config.ini avec 'SteamAppsPath'\nVeuillez verifier que le chemin amene bien vers workshop et common.\nSi cela ne fonctionne toujours place essayer 2\\ au lieu d'un seul."
        else:
            return "Problem in config.ini with 'SteamAppsPath'\nPlease check if in the path we have the repertories 'workshop' and 'common'.\nIf that's doesn't work try replace one \\ with two."

    def SuccessfulLoading(self=''):
        if Config.TranslateConfig == "fr":
            return "Chargement terminé avec succès!"
        else:
            return "Loading successfully completed!"

    def ErrorInstance(self=''):
        if Config.TranslateConfig == "fr":
            return 'Il y a un problème dans config.ini lié aux instances.\nVerifié si vos instances sont crées avec la forme: \n[INSTANCE1]\nWorshopList = 211,277\nModsList=None\nAussi si vous ne voulez pas charger de mods,écrivez "None" au lieu de rien.'
        else:
            return "Problem in config.ini link with instance.\nCheck if instance are created in this form: \n[INSTANCE1]\nWorshopList = 211,277\nModsList=None\nAlso if you don't want to load mod write 'None' and not nothing."

    def WorkshopError(self=''):
        if Config.TranslateConfig == "fr":
            return "Un problème a eu lieu lors de la modification des fichiers du workshop."
        else:
            return "Problem when trying to modify Workshop files."

    def ModError(self=''):
        if Config.TranslateConfig == "fr":
            return "Un problème a eu lieu lors de la modification des fichiers des Mods."
        else:
            return "Problem when trying to modify Mods files."

    def LaunchStarbound(self=''):
        if Config.TranslateConfig == "fr":
            return "Fermeture de Starbound..."
        else:
            return "Quit Starbound..."


def init():
    config = cp.ConfigParser()
    try:
        config.read_file(open('config.ini'))
    except:
        input(os.getcwd())
    Config.OriginPath = os.getcwd()
    Config.InstanceNumber = int(len(config.sections()[1:]))
    try:
        Config.Unstable = bool(config.get('OPTIONS', 'Unstable'))
    except:
        return Translate.UnstableBool()
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
        return Translate.SteamAppsPath()
    return Translate.SuccessfulLoading()


class Config:
    TranslateConfig = "en"
    Unstable = False
    InstanceNumber = 1
    SteamAppsPath = "D:\SteamLibrary\steamapps"
    OriginPath = ".\\"
    ShowMode = "1"


def pageShow(pgnb, modsList):
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
