package multibound;




import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

import javax.swing.JFrame;
import javax.swing.JPanel;

import org.ini4j.Ini;
import org.apache.log4j.Logger;





public class Launcheur{

	private static JPanel panel;
	private static JFrame frame;
	public static Logger log = Logger.getLogger(Logger.class.getName());
	
	public static void main(String[] args) {
		// Menu
		frame=new JFrame();
		panel=new Menu();
		frame.setVisible(true);
		frame.setLocationRelativeTo(null);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setContentPane(panel);
		// Initialisation
		if(!verifConfig()) {
			setPanel(new ConfigEditor("Steam Apps path error"));
		}
		try {
			LoadingBar.start();
		}catch (NullPointerException e){
			log.error("Unknow Error found in LoadingBar (Launcheur)");
			
		}

		/*frame.addComponentListener(new ComponentAdapter() 
		{  
		        public void componentResized(ComponentEvent evt) {
		            Component c = (Component)evt.getSource();
		            System.out.println(c);
		        }
		});*///TODO Resize dynamic
	}
	public static boolean verifConfig() {
		File log4j=new File("log4j.properties");
		if(!log4j.exists()) {
			String logprop="# Define the root logger with appender file\r\n" + 
			"log4j.rootLogger = DEBUG, FILE\r\n" + 
			"\r\n" + 
			"# Define the file appender\r\n" + 
			"log4j.appender.FILE=org.apache.log4j.FileAppender\r\n" + 
			"log4j.appender.FILE.File=files/logs/log.txt\r\n" + 
			"\r\n" + 
			"# Define the layout for file appender\r\n" + 
			"log4j.appender.FILE.layout=org.apache.log4j.PatternLayout\r\n" + 
			"log4j.appender.FILE.layout.conversionPattern=%-5p [%d{HH:mm:ss}]: %m%n";
			try {
				if(log4j.createNewFile()) {
					FileWriter myWriter = new FileWriter("log4j.properties");
					myWriter.write(logprop);
					myWriter.close();
					System.setProperty("java.util.logging.config.file",
				              "logging.properties");
					log = Logger.getLogger(Logger.class.getName());
				}
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		File storage=new File("files/storage.json");
		if(!storage.exists()) {
			//String storageCont="{\"1647206751\":\"[REDUX] Spawnable Item Pack - Frackin'Universe Patch\",\"751952122\":\"LowClueHunt-20\",\"111111\":\"\",\"1115847299.pak\":\"Grand Protector Robe\",\"942935636\":\"Ningen Race Mod ver 1.8 [Works with 1.4]\",\"733506855\":\"Pest Control\",\"1115847299\":\"Grand Protector Robe\",\"734855062\":\"Wardrobe Interface\",\"1181699750\":\"Reconstructor Addon\",\"749386227\":\"EverLana\",\"962379099\":\"Species Clothing\",\"1194878261\":\"[OFFICIAL] FU BYOS Modded Race Patch (FR Supported Races)\",\"1166322965\":\"Avali Themed Solar Power\",\"936735031\":\"Avali Augments And Assorments: Revisited\",\"1301992771\":\"Taehl's Teleport Beams\",\"960708990\":\"Hop On Shops\",\"729432341\":\"The Orcana\",\"741400551\":\"Less Annoying Weather\",\"936898205\":\"Skath Race\",\"1133678822\":\"New Protectorate Gear\",\"1617271676\":\"Stealth Cruiser -Hylotl-\",\"1117985463\":\"Improved Ship Encounter Descriptions\",\"1086875175.pak\":\"The Avali Matter Manipulator\",\"942632292\":\"No More Mech Helmet\",\"729427436\":\"Food Stack\",\"1154799233\":\"Armor Augments\",\"946335869\":\"Avali Drone Pet (1.3 Patch)\",\"970996345\":\"Starboy Handheld Games\",\"1633692250\":\"Top Tier Overhaul: Faithkeeper patch\",\"1102394541.pak\":\"Customizable Shuttlecraft\",\"762346800\":\"AAHP - Another Avian Hair Pack (Avian 'Hairstyles')\",\"1164332913\":\"Arachne Race\",\"1123927966\":\"Remote Interfaces\",\"1119973779\":\"Fixed Critters\",\"1410330646\":\"Make the Saturnians a Cuter Yet Mothy Race\",\"1465612579\":\"Avali heterochromia\",\"1394106904\":\"Solara, The Novakid Energy Sword\",\"733665104\":\"Spawnable Item Pack\",\"1112031234.pak\":\"Tabs for Avali Nanoloom\",\"1702704154\":\"Fragments of Ruin (Race)\",\"749382770\":\"EverPenguin\",\"729429063\":\"Felin\",\"1102394541\":\"Customizable Shuttlecraft\",\"1199374504\":\"Better Medical Scanner\",\"730960596\":\"Unlimited Active Crewmembers\",\"740750449\":\"Crew member race\\/gender\",\"1186075435\":\"Sticky Notes\",\"730849360\":\"The Pony Modpack\",\"1421523226\":\"What Menu?\",\"1475654005\":\"HOUND Fashion 0.9.1\",\"766773110\":\"Greckan Race Mod\",\"756688724\":\"Avali Heavy Mining Laser\",\"931058996\":\"Craftable Punchy\",\"1212882405\":\"[ALPHA] Project Blade Dance: Shortswords\",\"1793442129\":\"Platform Hatches - Avali Additions\",\"1363595896\":\"GoodTradeGoodsForFU\",\"931757634\":\"Craftable Concoctions\",\"733744908\":\"Avali mannequin\",\"740266309\":\"Time Control Tech\",\"1200004718\":\"Racial Drones\",\"963743678\":\"Avali Throwing Knives\",\"895140470\":\"NpcSpawner+\",\"1501869759\":\"I'd Like To Sit Here\",\"744621236\":\"Too Dumb to Live: Crew lava\\/poison immunity\",\"751868467\":\"Magic Labels\",\"817468961\":\"Melee Aiming\",\"743328719\":\"nonuniform\",\"1109772923\":\"Neko Alternate\",\"1169201536\":\"Avali SpecOps Additions\",\"1119066951\":\"Custom Messages\",\"729427744\":\"Instant Crafting\",\"1784813485\":\"Avali Weapon Type Additions(Reupload)\",\"736556366\":\"Access Granted\",\"1380941596\":\"Arsenalbound - Lastree Race Mod\",\"890205989\":\"Hat Mask Fixes\",\"1108897518\":\"The Bookstore\",\"1296666565\":\"Heartbeat\",\"1502658310\":\"The Forge: Protector's Broadsword+\",\"898712767\":\"Avali Objects+\",\"737027388\":\"Enhanced Chat Readability\",\"729439608\":\"Hunger Enabler for Casual Mode\",\"951696176\":\"Outpost Pet Healing Station\",\"729429377\":\"Felin Fur+\",\"1197841959\":\"Project Blade Dance: Broadswords - Legacy version\",\"1635522739\":\"More Outpost Objects\",\"751412690\":\"NoClueHunt\",\"1097047383\":\"Shadow Race 2.0!\",\"1723934741\":\"Non Fatal Fall Damage\",\"1410221883\":\"Bellatrix and Rigel\",\"1103338736\":\"Killable Villagers - Space Police version\",\"1639501560\":\"More Planet Info - FU Patch\",\"732276079\":\"The Viera of Ivalice\",\"729480149\":\"Frackin' Universe\",\"1543215897\":\"The Excalibur\",\"1426417593\":\"Idle Factories [Hiatus]\",\"729597107\":\"Familiars Race\",\"788890408\":\"Elunite Race\",\"1335123569\":\"Aetheric Book Creator\",\"737260577\":\"NyaaTech - Keypads\",\"823008631\":\"Character Creation Extender 100\",\"729524482\":\"Container UI Tweak\",\"1636662922\":\"Avali Plus\",\"1086875175\":\"The Avali Matter Manipulator\",\"1508762885\":\"Powers of Ruin\",\"747814787\":\"One Handed Hoe\",\"2010883172\":\"Project Knightfall\",\"2021492938\":\"Pokemon Plushies 2.0\",\"736134613\":\"Soma Exploration Ship (Avian)\",\"1109790315\":\"Codex - A bookstore addon\",\"1359257989\":\"Deerfolk Race Mod\",\"1643990804\":\"Taurikin Frackin' Races Patch\",\"729675474\":\"Avali Alternate Ship\",\"1390490083\":\"More NPC Ships\",\"1586956672\":\"Floran Fangs\",\"1372369380\":\"Wardrobe - Frackin' Universe\",\"850109963\":\"Elithian Races Mod\",\"730852387\":\"EverFrogg\",\"862287085\":\"Usable Bathtubs\",\"1628020624\":\"Skittle's Mega Crafter\",\"734173371\":\"Freedom of Movement\",\"1545962203\":\"The Forge: Healer's Toolkit\",\"729558042\":\"Avali (Triage) Race Mod\",\"730587191\":\"One-Handed Torch\",\"747774241\":\"Bug RNG Removal\",\"1276739133\":\"Improved Chat Bar\",\"1410203132\":\"Ori Moveset\",\"740613738\":\"B.Y.O.S. addon the Avali race (and tutorial)\",\"1175632845\":\"Valisocks\",\"1370155216\":\"Draconis Race Tweaks\",\"1546909574\":\"Erchius Crystal Module\",\"1292255989\":\"Custom Collections Frackin' Universe Patch\",\"834812331\":\"The Legacy Foods\",\"1112031234\":\"Tabs for Avali Nanoloom\",\"729558708\":\"Invisible Clothes\",\"1157929915\":\"Prop Pack\",\"760881689\":\"Custom Collections UI\",\"1750190964\":\"Maid NPCs\",\"1790667104\":\"EE for Starbound\",\"1253782150\":\"Player Dances and Emotes\",\"1408636770\":\"[OFFICIAL] FU BYOS Modded Race Patch (Races Without FR Support)\",\"730117759\":\"Novaskin\",\"1116521424\":\"Quest Reward UI Expansion\",\"902272423\":\"Penguin Piracy (SUSPENDED DEVELOPMENT)\",\"868165595\":\"Draconis Race(Humanoid Dragon Race)\",\"1383980456\":\"Blurplevali\",\"1495176820\":\"Avali more colors\",\"1103338736.pak\":\"Killable Villagers - Space Police version\",\"1120199994\":\"Orbis Pet (Apex)\",\"1611862131\":\"Military Outfit Pack\",\"1543219534\":\"Starbound Patch Project\",\"1372376485\":\"Wardrobe - Avali (Triage)\",\"1103027918\":\"The Saturnians\",\"1780994893\":\"Summer Sale Soda Mod\",\"822481787\":\"Hidden Armor\",\"1395844460\":\"SCP Foundation\",\"758705156\":\"Fixed Coffee Machine\",\"1229144124\":\"Swords Unite: Solarium Saber\",\"1694719307\":\"Merr-kin\",\"779096734\":\"Lamia Race\",\"1117007107\":\"More Planet Info (work with 1.4.X not guaranteed)\",\"751976722\":\"Avali Additions\",\"1778990370\":\"Avali Restored Tunics\",\"860578021\":\"Interactable Apex Pods\",\"770083792\":\"Hive Wasp Race\",\"1600522737\":\"Taurikin Race\",\"838356389\":\"Tenant Pack\",\"1250202824\":\"Python Railgun\",\"869900472\":\"Avali Perennial Crops\",\"731045482\":\"Avian Tail Feathers\",\"732452461\":\"Bunnykin Race\",\"1432794738\":\"avali camps on frackin' planets\",\"1382974058\":\"The Essential Delorean DMC12 Mod\",\"1088459034\":\"Quickbar Mini\",\"1381690033\":\"Blurple Everything- Discord Themed Character Colors and Dyes\",\"1404599095\":\"Make the Arachne a Cuter Race\",\"732697541\":\"Black Core Novakid\",\"853604555\":\"Themed Pet Tethers\",\"753337799\":\"Platform Hatches\",\"1412545702\":\"Spawnable Item Pack: Avali Patch\",\"1070172836\":\"Role-Play Emotes\",\"732277574\":\"Perennial Crops FU Compatibility Patch Edition\",\"763259329\":\"Frackin' Races\",\"744039259\":\"Shut Up Wesley\",\"742756612\":\"Novakid Dialogue\",\"730544933\":\"AnTiHair\",\"1131820988\":\"Tech Additions\",\"1405753979\":\"The Tenantator\",\"1774293331\":\"Borderlands Items Mod - 1.4 compatibility fix\",\"1088459034.pak\":\"Quickbar Mini\",\"746884345\":\"Expanded Magnorbs\",\"738313096\":\"Avali SpecOp Armor\",\"1258008544\":\"Backpacks\",\"730378641\":\"Perennial Crops\",\"1114465299\":\"Mech Deployment Beacons\",\"774083065\":\"Callistan Race Mod\",\"1086805718\":\"Low Health Alarm\",\"731220462\":\"Enhanced Storage\",\"894508987\":\"Incinerator\",\"730363398\":\"Efficient Watering\",\"1612579544\":\"Give the avian oculemonade\",\"750940532\":\"Bluedrop's Canine Companions\",\"1299446315\":\"The Essential Jetpack Mod\",\"1128426670\":\"Aimable Shields - Frackin Races compatible\",\"1590402990\":\"Solar Spectra - Radiant Novakid\",\"1103027918.pak\":\"The Saturnians\",\"1114822742\":\"Arsenalbound - Indix race pack\",\"1117007107.pak\":\"More Planet Info (work with 1.4.X not guaranteed)\",\"1265233462\":\"Boss Loot Bags\",\"802291314\":\"Skelekin Race\",\"1770003616\":\"Small Improvements 1.4 Edition\",\"1531978035\":\"Animal-like Hylotl Style\",\"729426722\":\"Xbawks Character Extender\",\"738601381\":\"Explorerpod\",\"1593802400\":\"Frackin' Universe - Melee Aiming\",\"792342404\":\"792342404.pak\"}";
			try {
				if(storage.createNewFile()) {
					FileWriter myWriter = new FileWriter("files/storage.json");
					myWriter.close();
				}
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		log.info("-------- Loading config.ini -------");
		try {
			Ini config = null;
			if(new File("files/config.ini").exists()) {
				config = new Ini(new File("files/config.ini"));
				if(new File(config.get("OPTIONS", "steamappspath")).exists()) {
					if(new File(config.get("OPTIONS", "steamappspath") + "\\common\\Starbound\\mods").exists()) {
						if(new File(config.get("OPTIONS", "steamappspath") + "\\workshop\\content\\211820").exists()) {
							//Initialisation finish
							log.info("-------- config.ini loaded successfully -------");
							return true;
						}else {
							//ERROR MODS PATH
							log.error("Workshop path error");
							return false;
						}
					}else {
						//ERROR MODS PATH
						log.error("Mods path error");
						return false;
					}
				}else {
					//ERROR STEAMAPPS PATH
					log.error("Steam Apps path error");
					return false;
				}
			}else {
				//CONFIG.INI NOT FOUND
				log.warn("Config.ini not found");
				File configF= new File("files/config.ini");
				if(configF.createNewFile()) {
					FileWriter myWriter = new FileWriter("files/config.ini");
					myWriter.write("[OPTIONS]\nsteamappspath = C:\\\\Program Files (x86)\\\\Steam\\\\steamapps\nunstable = False\nlanguage = en\neditormode = 1\n[INSTANCE1]\nname = Vanilla\nworkshoplist = None\nmodslist = None\nsavelocation = default\n");
					myWriter.close();
				}
				log.warn("config.ini created: But you should edit steamapps path");
				return verifConfig();
			}
		}catch (Exception e){
			log.error("Config.ini have problem with [OPTIONS] steamappspath");
			return false;
		}
	}

	public static void setPanel(JPanel panel) {
		frame.setContentPane(panel);
	}
	
	public static void setFrame(String title, int x,int y,int width,int height) {
		frame.setTitle(title);
		log.info("--------------------------------------");
		log.info(title+" are loading");
		frame.setBounds(x, y, width, height);
		frame.setLocationRelativeTo(null);
	}
	
	public static JFrame getFrame() {
		return frame;
	}
	//TODO Language

}
