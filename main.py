import configparser as cp
import os

class Config:
    TranslateConfig="en"
    Unstable=False
    InstanceNumber=1
    SteamAppsPath="D:\SteamLibrary\steamapps"
    OriginPath="D:\SteamLibrary\steamapps\common\Starbound\win64"
class Translate:
    def template(self):
        if Config.TranslateConfig=="fr":
            return
        else:
            return
    def loading(self):
        if Config.TranslateConfig=="fr":
            return "Chargement de votre Instance..."
        else:
            return "Loading of your instance..."
    def ChooseInstance(self):
        if Config.TranslateConfig=="fr":
            return "Choissisez l'instance que vous souhaitez:"
        else:
            return "Choose your instance:"
    def UnstableBool(self):
        if Config.TranslateConfig=="fr":
            return 'Il y a un problème dans config.ini avec "Unstable"\nVeuillez entrer "False" ou "True".'
        else:
            return 'Problem in config.ini with "Unstable"\nPlease enter "False" or "True".'
    def SteamAppsPath(self):
        if Config.TranslateConfig=="fr":
            return "Il y a un problème dans config.ini avec 'SteamAppsPath'\nVeuillez verifier que le chemin amene bien vers workshop et common.\nSi cela ne fonctionne toujours place essayer 2\\ au lieu d'un seul."
        else:
            return "Problem in config.ini with 'SteamAppsPath'\nPlease check if in the path we have the repertories 'workshop' and 'common'.\nIf that's doesn't work try replace one \\ with two."
    def SuccessfulLoading(self):
        if Config.TranslateConfig=="fr":
            return "Chargement terminé avec succès!"
        else:
            return "Loading successfully completed!"
    def ErrorInstance(self):
        if Config.TranslateConfig=="fr":
            return 'Il y a un problème dans config.ini lié aux instances.\nVerifié si vos instances sont crées avec la forme: \n[INSTANCE1]\nWorshopList = 211,277\nModsList=None\nAussi si vous ne voulez pas charger de mods,écrivez "None" au lieu de rien.'
        else:
            return "Problem in config.ini link with instance.\nCheck if instance are created in this form: \n[INSTANCE1]\nWorshopList = 211,277\nModsList=None\nAlso if you don't want to load mod write 'None' and not nothing."
    def WorkshopError(self):
        if Config.TranslateConfig=="fr":
            return "Un problème a eu lieu lors de la modification des fichiers du workshop."
        else:
            return "Problem when trying to modify Workshop files."
    def ModError(self):
        if Config.TranslateConfig=="fr":
            return "Un problème a eu lieu lors de la modification des fichiers des Mods."
        else:
            return "Problem when trying to modify Mods files."
    def LaunchStarbound(self):
        if Config.TranslateConfig=="fr":
            return "Fermeture de Starbound..."
        else:
            return "Quit Starbound..."



def init():
    config = cp.ConfigParser()
    try:
        config.read_file(open('config.ini'))
    except:
        input(os.getcwd())
    Config.OriginPath=os.getcwd()
    Config.InstanceNumber=int(len(config.sections()[1:]))
    try:
        Config.Unstable = bool(config.get('OPTIONS', 'Unstable'))
    except:
        return Translate.UnstableBool("")
    if config.get('OPTIONS','Language')!="en" and config.get('OPTIONS','Language') in ("fr"):
        Config.TranslateConfig = config.get('OPTIONS','Language')
    try:
        SteamAppsPath=config.get('OPTIONS','SteamAppsPath')
        os.chdir(SteamAppsPath+"\\workshop\content\\211820")
        os.chdir(SteamAppsPath+"\\common\Starbound") #Unstable change todo
        os.chdir(SteamAppsPath)
        Config.SteamAppsPath = SteamAppsPath
        os.chdir(Config.OriginPath)
    except:
        return Translate.SteamAppsPath("")
    return Translate.SuccessfulLoading("")
def ChooseYourInstance(dic):
    try:
        print(Translate.ChooseInstance(""))
        for i in range(0,len(dic)):
            print(str(i+1)+" "+dic['Instance'+str(i+1)][0])
    except:
        return Translate.ErrorInstance("")
    try:
        choice=int(input(Translate.ChooseInstance("")))
        if choice not in range(1,len(dic)+1):
            return ChooseYourInstance(dic)
        else:
            return Translate.loading(''),choice,dic
    except:
        return ChooseYourInstance(dic)
def LoadingInstance():
    config = cp.ConfigParser()
    config.read_file(open('config.ini'))
    dic={}
    try:
        for i in range(0,Config.InstanceNumber):
            dic['Instance'+str(i+1)]= config.get('INSTANCE'+str(i+1),'Name'),config.get('INSTANCE'+str(i+1),'workshoplist'),config.get('INSTANCE'+str(i+1),'ModsList')
    except:
        return Translate.ErrorInstance('')
    return ChooseYourInstance(dic)
def directSearch(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]
def InstanceAppli(ch,dic):
    InstanceLoad=dic['Instance'+str(ch)]
    Workshop=InstanceLoad[1].split(',')
    ModLoad=InstanceLoad[2].split(',')
    try:
        direc=directSearch(Config.SteamAppsPath+"\\workshop\content\\211820")
        os.chdir(Config.SteamAppsPath+"\\workshop\content\\211820")
        for i in range(0,len(direc)):
            if direc[i] not in Workshop and "Disabled." not in direc[i]:
                os.rename(direc[i],"Disabled."+str(direc[i]))
        for i in range(0,len(Workshop)):
            if ("Disabled."+Workshop[i]) in direc:
                os.rename("Disabled."+Workshop[i],Workshop[i])
    except:
        return Translate.WorkshopError
    try:
        direc=directSearch(Config.SteamAppsPath+"\\common\Starbound\mods")
        os.chdir(Config.SteamAppsPath + "\\common\Starbound\mods")
        for i in range(0,len(direc)):
            if direc[i] not in ModLoad and "Disabled." not in direc[i]:
                os.rename(direc[i],".Disabled."+str(direc[i]))
        for i in range(0,len(ModLoad)):
            if (".Disabled."+ModLoad[i]) in direc:
                os.rename(".Disabled."+ModLoad[i],ModLoad[i])
    except:
        return Translate.ModError
    os.system(Config.SteamAppsPath+'\\common\Starbound\win64\Starbound.exe')
    return Translate.LaunchStarbound("")
def ListeCreator(dic):
    AllName=[]
    for i in range(0,len(dic)):
        AllName.append(dic['Instance'+str(i+1)][0])
    return AllName

print(init())
inst=LoadingInstance()
print(inst[0])
InstanceAppli(inst[1],inst[2])
#Todo : Support Collection, Inteface Graphique avec Nom et Image
