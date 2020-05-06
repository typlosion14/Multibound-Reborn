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

import org.ini4j.Ini;
import org.ini4j.InvalidFileFormatException;

public class LoadingBar extends JFrame {
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	private JProgressBar progressBar;
	public static MonSwingWorker swingWorker;

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
				e.printStackTrace();
				return null;
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
				return null;
			}

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
			for (int i = 0; i < simpleArray.length; i++) {
				list[i] = new Mods(simpleArray[i], false);
				setProgress(i/simpleArray.length*100);
				progressBar.setValue(i);
			}
			setProgress(0);
			progressBar.setValue(0);
			try {
				config = new Ini(new File("files/config.ini"));
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			try {
				File test = new File(config.get("OPTIONS", "steamappspath"));
				test.getName();
			} catch (NullPointerException e) {
				;
			}
			try {
				folder = new File(config.get("OPTIONS", "steamappspath") + "\\common\\Starbound\\mods");

			} catch (Exception e) {
				;
			}
			listFiles = new ArrayList<String>();
			for (File file : folder.listFiles()) {
				if (file.isDirectory() || file.getName().endsWith(".pak")) {
					listFiles.add(file.getName());
				}
			}
			simpleArray = new String[listFiles.size()];
			listFiles.toArray(simpleArray);
			progressBar.setMaximum(simpleArray.length);
			list = new Mods[simpleArray.length];
			for (int i = 0; i < simpleArray.length; i++) {
				list[i] = new Mods(simpleArray[i], true);
				setProgress(i/simpleArray.length*100);
				progressBar.setValue(i);

			}
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