import configparser as cp
import os
import pygame
from urllib.request import urlopen, Request
from PIL import Image

class Config:
    TranslateConfig="en"
    Unstable=False
    InstanceNumber=1
    SteamAppsPath="D:\SteamLibrary\steamapps"
    OriginPath=".\\"
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
            dic['Instance'+str(i+1)]= config.get('INSTANCE'+str(i+1),'Name'),config.get('INSTANCE'+str(i+1),'WorshopList'),config.get('INSTANCE'+str(i+1),'ModsList')
    except:
        return Translate.ErrorInstance('')
    return Translate.loading(''),dic
def directSearch(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]
def InstanceAppli(ch,dic):
    pygame.quit()
    #for i in range(0,len(dic)):
    #    if dic['Instance'+str(i+1)][0]==ch:
    #        InstanceLoad = dic['Instance'+str(i+1)]
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
def LaunchPygame(dic):
    inProgress = True
    # Initialisation de pygame
    CYAN = (0, 255, 255)
    pygame.init()
    Fond_Ecran = pygame.display.set_mode((1000, 800))  # Taille de la fenetre (en pixel)
    pygame.display.set_caption("Multibound Reborn")  # Nom de la fenetre
    Font = pygame.font.Font(None, 32)
    imageL=pygame.image.load(Config.OriginPath+"/textures/Fond.png")
    Fond_Ecran.blit(imageL,(0,0))
    Fond_Ecran.blit(Font.render("Choissisez une instance :", 1, CYAN), (1000/2-(11*len("Choissisez une instance :")), 0))

    if int(Config.InstanceNumber/4)>=1:
        for y in range(0,int(Config.InstanceNumber/4)):
            for i in range(0,Config.InstanceNumber):
                Fond_Ecran.blit(Font.render(dic['Instance'+str(i+1)][0], 1, CYAN), (250*i+1, y+1*64))
    else:
        for i in range(0, Config.InstanceNumber):
            Fond_Ecran.blit(Font.render(dic['Instance' + str(i + 1)][0], 1, CYAN), (250 * i + 1, 64))
    pygame.display.update()
    while inProgress:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if int(Config.InstanceNumber / 4) >= 1:
                    for y in range(0, int(Config.InstanceNumber / 4)):
                        for i in range(0, Config.InstanceNumber):
                            if (250 * i + 1)<pos[0]<(250 * (i + 2)) and (y + 1 * 64)<pos[1]<(y + 2 * 64+32):
                                print(pos)
                                return InstanceAppli(i+1, dic)
                else:
                    for i in range(0, Config.InstanceNumber):
                        if (250 * i + 1) < pos[0] < (250 * (i + 2)) and (64) < pos[1] < (96):
                            print(pos)
                            return InstanceAppli(i + 1, dic)
            if event.type == pygame.QUIT:
                return False

print(init())
inst=LoadingInstance()
print(inst[0])
print(LaunchPygame(inst[1]))
#Todo : Support Collection, Inteface Graphique avec Nom et Image, Createur d'instance