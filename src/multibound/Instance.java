package multibound;


import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Dictionary;
import java.util.Hashtable;
import java.util.regex.Pattern;

import javax.swing.JLabel;

import org.apache.log4j.Logger;
import org.ini4j.Ini;

public class Instance {
	private int nb;
	private String name;
	private String savelocation, modslist, workshoplist;
	public static Logger log = Logger.getLogger(Logger.class.getName());

	Instance(int nb) {
		Ini config = new Ini();
		try {
			config = new Ini(new File("files/config.ini"));
		} catch (IOException e) {
			// TODO Auto-generated catch block
			log.warn("Config.ini not found (Instance)");
			e.printStackTrace();
		}
		this.nb = nb;
		this.name = config.get("INSTANCE" + nb, "name");
		log.debug("Instance name: "+this.name);
		this.modslist = config.get("INSTANCE" + nb, "modslist");
		log.debug("Instance ModsList: "+this.modslist);
		this.workshoplist = config.get("INSTANCE" + nb, "workshoplist");
		log.debug("Instance WorkshopList: "+this.workshoplist);
		this.savelocation = config.get("INSTANCE" + nb, "savelocation");
		log.debug("Instance Save Location: "+this.savelocation);
	}

	public int getNumber() {
		return nb;
	}

	public String getName() {
		return name;
	}

	public String getSaveLocation() {
		if (savelocation == null) {
			return "default";
		}
		return savelocation;
	}

	public Mods[] getModsList() {
		log.debug(this.name+" getModsList start");
		if (modslist.split(",").length == 1 && modslist.split(",")[0].contains("None")) {
			return new Mods[0];
		}
		String[] simpleArray = modslist.split(",");
		Mods[] list = new Mods[simpleArray.length];
		for (int i = 0; i < simpleArray.length; i++) {
			list[i] = new Mods(simpleArray[i], true);
		}
		Arrays.sort(list);
		log.debug(this.name+" getModsList finish");
		return list;
	}

	public Mods[] getWorkshopList() {
		log.debug(this.name+" getWorkshopList start");
		if (workshoplist.split(",").length == 1 && workshoplist.split(",")[0].contains("None")) {
			return new Mods[0];
		}
		String[] simpleArray = workshoplist.split(",");
		Mods[] list = new Mods[simpleArray.length];
		for (int i = 0; i < simpleArray.length; i++) {
			list[i] = new Mods(simpleArray[i], false);
		}
		Arrays.sort(list);
		log.debug(this.name+" getWorkshopList finish");
		return list;
	}

	public static int getInstanceNb() {
		String contents = "";
		try {
			contents = new String(Files.readAllBytes(Paths.get("files/config.ini")));
		} catch (IOException e) {
			log.warn("Config.ini not found (Instance.getInstanceNb)");
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		log.debug("getInstanceNb loaded");
		return (contents.split(Pattern.quote("[INSTANCE"), -1).length) - 1;// TODO regex ;_;[INSTANCE([0-9]|[0-9][0-9])]
	}

	public static Dictionary<String, Integer> getDicNameId() {// Dictionnaire pour avoir Instance Name : Instance ID
		Ini config = null;
		try {
			config = new Ini(new File("files/config.ini"));
		} catch (IOException e) {
			log.warn("Config.ini not found (Instance.getDicNameId)");
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		Dictionary<String, Integer> dic = new Hashtable<String, Integer>();
		for (int i = 1; i < getInstanceNb() + 1; i++) {
			dic.put(config.get("INSTANCE" + i, "name"), i);
		}
		log.debug("getDicNameId finish");
		return dic;

	}

	public static String[] getListName() {// Obtenir tous les noms des instances
		String[] list = new String[getInstanceNb()];
		Ini config = null;
		try {
			config = new Ini(new File("files/config.ini"));
		} catch (IOException e) {
			log.warn("Config.ini not found (Instance.getListName)");
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		for (int i = 0; i < getInstanceNb(); i++) {
			list[i] = config.get("INSTANCE" + (i + 1), "name");
		}
		log.debug("getListName finish");
		return list;
	}

	public static Mods[] getModsFile(JLabel warningText) {
		log.debug("getModsFile start");
		File folder = null;
		Ini config = null;
		try {
			config = new Ini(new File("files/config.ini"));
		} catch (IOException e) {
			log.warn("Config.ini not found (Instance.getModsFile)");
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		try {
			File test = new File(config.get("OPTIONS", "steamappspath"));
			test.getName();
		} catch (NullPointerException e) {
			warningText.setText("SteamPath ERROR MODS");
		}
		try {
			folder = new File(config.get("OPTIONS", "steamappspath") + "\\common\\Starbound\\mods");

		} catch (Exception e) {
			warningText.setText("GET FILE ERROR MODS");
		}
		ArrayList<String> listFiles = new ArrayList<String>();
		for (File file : folder.listFiles()) {
			if (file.isDirectory() || file.getName().endsWith(".pak")) {
				listFiles.add(file.getName());
			}
		}
		String[] simpleArray = new String[listFiles.size()];
		listFiles.toArray(simpleArray);
		Mods[] list = new Mods[simpleArray.length];

		for (int i = 0; i < simpleArray.length; i++) {
			list[i] = new Mods(simpleArray[i], true);

		}

		Arrays.sort(list);
		log.debug("getModsFile finish");
		return list;
	}

	public static Mods[] getWorkshopFile(JLabel warningText) {
		log.debug("getWorkshopFile start");
		File folder = null;
		Ini config = null;
		try {
			config = new Ini(new File("files/config.ini"));
		} catch (IOException e) {
			log.warn("config.ini can't be found (Instance)");
			e.printStackTrace();
			warningText.setText("config.ini can't be found");
		}
		try {
			File test = new File(config.get("OPTIONS", "steamappspath"));
			test.getName();
			System.out.println(test);
		} catch (NullPointerException e) {
			log.warn("SteamPath ERROR can't be found");
			warningText.setText("SteamPath ERROR WORKSHOP");
		}
		try {
			folder = new File(config.get("OPTIONS", "steamappspath") + "\\workshop\\content\\211820");

		} catch (Exception e) {
			log.warn("Workshop Path ERROR can't be found");
			warningText.setText("GET FILE ERROR WORKSHOP");
		}
		log.info("config.ini should work");
		ArrayList<String> listFiles = new ArrayList<String>();
		for (File file : folder.listFiles()) {
			log.debug(file);
			if (file.isDirectory()) {
				listFiles.add(file.getName());
			}
		}
		String[] simpleArray = new String[listFiles.size()];
		listFiles.toArray(simpleArray);
		Mods[] list = new Mods[simpleArray.length];
		for (int i = 0; i < simpleArray.length; i++) {
			list[i] = new Mods(simpleArray[i], false);
		}
		Arrays.sort(list);
		log.debug("getWorkshopFile finish");
		return list;
	}

	public Mods[] getDesactivedWorskshop(JLabel warningText) {
		log.debug(this.name+" getDesactivedWorskshop start");
		Mods[] wki = getWorkshopFile(warningText);
		Mods[] wka = getWorkshopList();
		ArrayList<Mods> r = new ArrayList<Mods>();
		for (int i = 0; i < wki.length; i++) {
			if (!contain(wka, wki[i])) {
				r.add(wki[i]);
			}
		}
		Mods[] b = r.toArray(new Mods[r.size()]);
		Arrays.sort(b);
		log.debug(this.name+" getDesactivedWorskshop finish");
		return b;

	}

	public Mods[] getDesactivedMods(JLabel warningText) {
		log.debug(this.name+" getDesactivedMods start");
		Mods[] wki = getModsFile(warningText);
		Mods[] wka = getModsList();
		ArrayList<Mods> r = new ArrayList<Mods>();
		for (int i = 0; i < wki.length; i++) {
			if (!contain(wka, wki[i])) {
				r.add(wki[i]);
			}
		}
		Mods[] b = r.toArray(new Mods[r.size()]);
		Arrays.sort(b);
		log.debug(this.name+" getDesactivedMods finish");
		return b;

	}

	public boolean contain(Mods[] arr, Mods look) {
		for (int i = 0; i < arr.length; i++) {
			if (arr[i].isMod()) {
				if (arr[i].getName() == look.getName()) {
					return true;
				}
			} else {
				if (arr[i].getId() == look.getId()) {
					return true;
				}
			}

		}
		return false;
	}
}
