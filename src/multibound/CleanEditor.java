package multibound;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;

import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.SwingConstants;

import org.ini4j.Ini;

public class CleanEditor extends JPanel implements ActionListener {
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	JButton clean_btn, back_btn, clean_btn_save;

	CleanEditor() {
		Launcheur.setFrame("Multibound Reborn - Clean Files", 100, 100, 361, 175);
		setBounds(100, 100, 361, 175);
		setLayout(null);

		JLabel title = new JLabel("Clean files");
		title.setHorizontalAlignment(SwingConstants.CENTER);
		title.setBounds(119, 11, 108, 14);
		add(title);

		JLabel warning_label = new JLabel("You're about to clean files mods.");
		warning_label.setHorizontalAlignment(SwingConstants.CENTER);
		warning_label.setBounds(36, 36, 274, 25);
		add(warning_label);

		JLabel label_1 = new JLabel(" if you want uninstall Multibound Reborn it's imperative.");
		label_1.setHorizontalAlignment(SwingConstants.CENTER);
		label_1.setBounds(24, 64, 285, 14);
		add(label_1);

		back_btn = new JButton("Cancel");
		back_btn.setBounds(36, 91, 89, 23);
		add(back_btn);

		clean_btn = new JButton("Mods");
		clean_btn.setBounds(221, 91, 89, 23);
		add(clean_btn);
		
		clean_btn_save = new JButton("Save");
		clean_btn_save.setBounds(129, 91, 89, 23);
		add(clean_btn_save);

		back_btn.addActionListener(this);
		clean_btn.addActionListener(this);
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		Object source=e.getSource();
		if (source.equals(back_btn)) {
			Launcheur.setPanel(new Menu());
		} else if (source.equals(clean_btn)){
			clean();
			
		} else if (source.equals(clean_btn_save)){
			cleanSave();
		}

	}

	static public void clean() {
		Ini config = null;
		try {
			config = new Ini(new File("files/config.ini"));
		} catch (IOException error) {
			// TODO Auto-generated catch block
			error.printStackTrace();
		}
		File folder = new File(config.get("OPTIONS", "steamappspath") + "\\workshop\\content\\211820");
		for (File file : folder.listFiles()) {
			if (file.getName().contains("Disabled")) {
				if (file.getName().contains(".Disabled.")) {
					file.renameTo(new File(file.getName().replace(".Disabled.", "")));
				} else {
					file.renameTo(new File(file.getName().replace("Disabled.", "")));
				}
			}
		}
		folder = new File(config.get("OPTIONS", "steamappspath") + "\\common\\Starbound\\mods");
		for (File file : folder.listFiles()) {
			if (file.getName().contains("Disabled")) {
				if (file.getName().contains(".Disabled.")) {
					file.renameTo(new File(file.getName().replace(".Disabled.", "")));
				} else {
					file.renameTo(new File(file.getName().replace("Disabled.", "")));
				}
			}
		}
	}

	static public void cleanSave() {
		// TODO cleanSave
		Ini config = null;
		try {
			config = new Ini(new File("files/config.ini"));
		} catch (IOException error) {
			// TODO Auto-generated catch block
			error.printStackTrace();
		}
		String steampath = config.get("OPTIONS", "steamappspath");
		for (File f : new File(steampath + "\\common\\Starbound\\InstanceSave").listFiles()) {
			for (File f2 : f.listFiles()) {
				if (f2.isDirectory()) {
					for (File f3 : f.listFiles()) {
						try {
							Files.move(f3.toPath(), new File(
									steampath + "\\common\\Starbound\\storage\\" + f2.getName() + "\\" + f3.getName())
											.toPath());
						} catch (IOException e) {
							// TODO Auto-generated catch block
							e.printStackTrace();
						}
					}

				}
			}
		}

	}
}
