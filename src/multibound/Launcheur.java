package multibound;




import java.io.File;

import javax.swing.JFrame;
import javax.swing.JPanel;

import org.apache.log4j.Logger;
import org.ini4j.Ini;





public class Launcheur{

	private static JPanel panel;
	private static JFrame frame;
	public static Logger log = Logger.getLogger(Logger.class.getName());
	
	public static void main(String[] args) {
		// Initialisation
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
						}else {
							//ERROR MODS PATH
							log.error("Workshop path error");
						}
					}else {
						//ERROR MODS PATH
						log.error("Mods path error");
					}
				}else {
					//ERROR STEAMAPPS PATH
					log.error("Steam Apps path error");
				}
			}else {
				//CONFIG.INI NOT FOUND
				log.error("Config.ini not found");
			}
		}catch (Exception e){
			log.error("Config.ini have problem with [OPTIONS] steamappspath");
		}
		try {
			LoadingBar.start();
		}catch (NullPointerException e){
			log.error("Unknow Error found in LoadingBar (Launcheur)");
			
		}
		// Menu
		frame=new JFrame();
		panel=new Menu();
		frame.setVisible(true);
		frame.setLocationRelativeTo(null);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setContentPane(panel);
		/*frame.addComponentListener(new ComponentAdapter() 
		{  
		        public void componentResized(ComponentEvent evt) {
		            Component c = (Component)evt.getSource();
		            System.out.println(c);
		        }
		});*///TODO Resize dynamic
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
