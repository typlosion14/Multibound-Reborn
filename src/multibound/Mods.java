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

import org.ini4j.Ini;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

public class Mods implements Comparable<Mods> {
	int id;
	String name;
	String filename;
	boolean isMod;
	
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
					this.id = 0;
				}
			} else {
				this.id = 0;
			}

		}
		this.name = IniName();
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
		} catch (IOException e) {
			e.printStackTrace();
		}
		return "Error";
	}

	@SuppressWarnings("unchecked")
	private String IniName() {
		JSONParser parser = new JSONParser();
		JSONObject jsonObject = null;
		String title = null;
		try (Reader reader = new FileReader("files/storage.json")) {//On verifie que c'est pas dans le JSON
			jsonObject = (JSONObject) parser.parse(reader);
			// String name = (String) jsonObject.get("name");
		} catch (IOException e) {
			e.printStackTrace();
		} catch (ParseException e) {
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
			}else {
				jsonObject.put(Integer.toString(id), filename);//Un nom n'est pas trouvé
			}
			try (FileWriter file = new FileWriter("files/storage.json")) {
				file.write(jsonObject.toJSONString());
			} catch (IOException e) {
				e.printStackTrace();
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
