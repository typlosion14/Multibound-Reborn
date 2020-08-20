package multibound;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.Reader;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLConnection;

import org.apache.log4j.Logger;
import org.ini4j.Ini;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

public class Mods implements Comparable<Mods> {
	private int id;
	private String name;
	private String filename;
	private boolean isMod;
	public static Logger log = Logger.getLogger(Logger.class.getName());
	

	
	Mods(String id, boolean isMod) {
		this.isMod = isMod;
		if (!isMod) {
			this.id = Integer.parseInt(id);
		} else {
			this.filename = id;
			if (id.contains(".pak")) {
				try {
					this.id = Integer.parseInt(id.replace(".pak", ""));
				} catch (Exception e) {
					log.debug(id+" is not a pak file (Mods)");
					this.id = 0;
				}
			} else {
				this.id = 0;
			}

		}
		this.name = iniName();
	}

	public String getFilename() {
		if (isMod) {
			return filename;
		}
		return Integer.toString(id);

	}

	public int getId() {
		return id;
	}

	public String getName() {
		return name;
	}

	public boolean isMod() {
		return isMod;
	}

	static public String getHtml(String a) {

		try {
			// get URL content
			URL url = new URL(a);
			URLConnection conn = url.openConnection();

			// open the stream and put it into BufferedReader
			BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream()));

			String inputLine;
			String Lines = "";
			while ((inputLine = br.readLine()) != null) {
				Lines += inputLine;
			}
			br.close();

			return Lines;

		} catch (MalformedURLException e) {
			e.printStackTrace();
			log.debug(a+" workshop id (url) is not correct (Mods)");
		} catch (IOException e) {
			e.printStackTrace();
			log.debug(a+" workshop id (IO) is not correct (Mods)");
		}
		log.error("Error unknown with getHtml("+a+") for workshop id (Mods)");
		return "Error";
	}

	@SuppressWarnings("unchecked")
	private String iniName() {
		JSONParser parser = new JSONParser();
		JSONObject jsonObject = null;
		String title = null;
		try (Reader reader = new FileReader("files/storage.json")) {//On verifie que c'est pas dans le JSON
			jsonObject = (JSONObject) parser.parse(reader);
			// String name = (String) jsonObject.get("name");
		} catch (IOException e) {
			log.warn("storage.json not found (Mods)");
			e.printStackTrace();
		} catch (ParseException e) {
			log.error("storage.json can't be readed");
			log.error("try to look with a JSON Viewer for fix it");
			e.printStackTrace();
		}
		if (id != 0) {
			title = (String) jsonObject.get(Integer.toString(id));
		} else {
			return filename;
		}

		if (title == null) {//Si c'est pas dans le JSON
			String html = getHtml("https://steamcommunity.com/sharedfiles/filedetails/?id=" + id);
			int pos1 = html.indexOf("<div class=\"workshopItemTitle\">");
			title = html.substring(pos1 + "<div class=\"workshopItemTitle\">".length(), html.indexOf("</div>", pos1));
			if (!title.contains("html")) {
				jsonObject.put(Integer.toString(id), title);//Un nom est trouvé
				log.info("Name found");
			}else {
				jsonObject.put(Integer.toString(id), filename);//Un nom n'est pas trouvé
				log.info("Name not found (use filename)");
			}
			try (FileWriter file = new FileWriter("files/storage.json")) {
				file.write(jsonObject.toJSONString());
				log.info("Name writed in storage.json");
			} catch (IOException e) {
				e.printStackTrace();
				log.warn("storage.json not found (Mods)");
			}
		}
		if (!isMod) {
			return title;
		} else {
			if (title.contains("html")) {
				return filename.replace(".Disabled.", "").replace(".disabled","");
			}
			try {
				Ini ini = new Ini(new File("files\\config.ini"));
				String editormode=ini.get("OPTIONS", "editormode");
				switch (editormode) {
				case "1":
					return filename.replace(".Disabled.", "").replace(".disabled","")+" - "+ title;
				case "2":
					return filename.replace(".Disabled.", "").replace(".disabled","");
				case "3":
					return title;
				default:
					return title+" - "+ filename.replace(".Disabled.", "").replace(".disabled","");
				}
			} catch (IOException e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
				log.warn("config.ini not found (Mods)");
				return title+" - "+ filename.replace(".Disabled.", "").replace(".disabled","");
				
			}
			
		}

	}

	@Override
	public String toString() {
		return name;
	}

	@Override
	public int compareTo(Mods arg0) {
		return getName().compareTo(arg0.getName());
	}
}
