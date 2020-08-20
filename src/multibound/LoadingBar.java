package multibound;

import java.awt.BorderLayout;
import java.awt.Cursor;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JProgressBar;
import javax.swing.SwingWorker;

import org.apache.log4j.Logger;
import org.ini4j.Ini;
import org.ini4j.InvalidFileFormatException;

public class LoadingBar extends JFrame {
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	private JProgressBar progressBar;
	public static MonSwingWorker swingWorker;
	public static Logger log = Logger.getLogger(Logger.class.getName());

	class MonSwingWorker extends SwingWorker<Integer, String> {
		JFrame marcehsp;

		public MonSwingWorker(JFrame oskour) {
			/* On ajoute un écouteur de barre de progression. */
			this.marcehsp=oskour;
		}

		@Override
		public Integer doInBackground() {
			Ini config = null;
			File folder = null;
			try {
				config = new Ini(new File("files/config.ini"));
				folder = new File(config.get("OPTIONS", "steamappspath") + "\\workshop\\content\\211820");
			} catch (InvalidFileFormatException e) {
				// TODO Auto-generated catch block
				log.warn("config.ini Invalid File Format (LoadingBar)");
				e.printStackTrace();
				return null;
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
				log.warn("config.ini not found (LoadingBar)");
				return null;
			}
			log.info("get Workshop Mods list LoadingBar");
			ArrayList<String> listFiles = new ArrayList<String>();
			for (File file : folder.listFiles()) {
				if (file.isDirectory()) {
					
					listFiles.add(file.getName());
				}
			}
			
			String[] simpleArray = new String[listFiles.size()];
			listFiles.toArray(simpleArray);
			progressBar.setMaximum(simpleArray.length);
			Mods[] list = new Mods[simpleArray.length];
			log.info("Start loading Workshop Mods  (LoadingBar)");
			for (int i = 0; i < simpleArray.length; i++) {
				list[i] = new Mods(simpleArray[i], false);
				setProgress(i/simpleArray.length*100);
				progressBar.setValue(i);
			}
			log.info("Loading Workshop Mods is successful  (LoadingBar)");
			setProgress(0);
			progressBar.setValue(0);
			try {
				if (new File("files/config.ini").exists()) {
					config = new Ini(new File("files/config.ini"));
				}else {
					log.error("config.ini not found (LoadingBar)");
				}
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
				log.error("config.ini not found (LoadingBar)");
			}
			if (new File(config.get("OPTIONS", "steamappspath")).exists()) {
				
			}else {
				log.error("Steam Apps Path don't exist (LoadingBar)");
			}
			try {
				if(new File(config.get("OPTIONS", "steamappspath") + "\\common\\Starbound\\mods").exists()) {
					folder = new File(config.get("OPTIONS", "steamappspath") + "\\common\\Starbound\\mods");
				}else {
					log.error("Starbound/mods path is not correct (LoadingBar)");
				}
			} catch (NullPointerException e) {
				log.error("Starbound/mods path is not correct (LoadingBar)");
			}
			log.info("get Mods list (LoadingBar)");
			listFiles = new ArrayList<String>();
			for (File file : folder.listFiles()) {
				if (file.isDirectory() || file.getName().endsWith(".pak")) {
					listFiles.add(file.getName());
					log.debug(file.getName()+" found");
				}
			}
			simpleArray = new String[listFiles.size()];
			listFiles.toArray(simpleArray);
			progressBar.setMaximum(simpleArray.length);
			list = new Mods[simpleArray.length];
			log.info("Start loading Mods LoadingBar (LoadingBar)");
			for (int i = 0; i < simpleArray.length; i++) {
				list[i] = new Mods(simpleArray[i], true);
				setProgress(i/simpleArray.length*100);
				progressBar.setValue(i);

			}
			log.info("Loading Mods is successful (LoadingBar)");
			done();
			return 0;
		}

		@Override
		protected void process(List<String> strings) {
			
		}

		@Override
		protected void done() {
			try {
				/* Le traitement est terminé. */
				setProgress(100);
				marcehsp.setVisible(false);
				marcehsp.dispose();


			} catch (Exception e) {
				log.warn("LoadingBar can't be termined (LoadingBar)");
				e.printStackTrace();
			}

		}

	}

	public LoadingBar() {
		/* Construction de l'interface graphique. */
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		progressBar = new JProgressBar();
		JPanel content = new JPanel(new BorderLayout());
		setCursor(new Cursor(Cursor.WAIT_CURSOR));
		JLabel textArea = new JLabel("Loading Mods...");
		content.add(textArea);
		JPanel south = new JPanel(new BorderLayout());
		south.add(progressBar);
		content.add(south, BorderLayout.SOUTH);
		setContentPane(content);
		pack();
		setLocation(100, 100);
		setVisible(true);
	}

	static public void start() {
		LoadingBar demo = new LoadingBar();
		swingWorker = demo.new MonSwingWorker(demo);
		swingWorker.doInBackground();
		

	}

	public static void main(String... args) {
		start();
	}

}