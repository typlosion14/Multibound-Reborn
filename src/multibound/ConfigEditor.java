package multibound;

import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.IOException;

import javax.swing.DefaultComboBoxModel;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JFileChooser;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.SwingConstants;

import org.apache.log4j.Logger;
import org.ini4j.Ini;

public class ConfigEditor extends JPanel implements ActionListener, Panel {

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	private JButton back_btn= new JButton("ERROR"),
			save_btn= new JButton("ERROR");
	private JFileChooser fc;
	private JLabel txtWarning;
	private String[] comboLanguage ={ "en", "fr" },
		comboName={  "Steam Name - filename", "filename - Steam Name", "filename", "Steam Name"  };
	private JComboBox<String> comboBoxN,
		comboBoxL;
	private String filepath=null;
	public static Logger log = Logger.getLogger(Logger.class.getName());

	ConfigEditor() {
		Launcheur.setFrame("Multibound Reborn - Config", 100, 100, 361, 342);
		setBounds(100, 100, 361, 342);
		setLayout(null);

		JLabel title = new JLabel("Config Options");
		title.setHorizontalAlignment(SwingConstants.CENTER);
		title.setBounds(119, 11, 108, 14);
		add(title);

		JLabel lblNewLabel = new JLabel("Language:");
		lblNewLabel.setHorizontalAlignment(SwingConstants.CENTER);
		lblNewLabel.setBounds(50, 61, 91, 14);
		add(lblNewLabel);
		
		comboBoxL = new JComboBox<String>();
		comboBoxL.setModel(new DefaultComboBoxModel<String>(comboLanguage));
		comboBoxL.setBounds(169, 58, 84, 20);
		add(comboBoxL);

		JLabel lblNewLabel_1 = new JLabel("How to display:");
		lblNewLabel_1.setHorizontalAlignment(SwingConstants.CENTER);
		lblNewLabel_1.setBounds(50, 118, 91, 14);
		add(lblNewLabel_1);
		
		comboBoxN = new JComboBox<String>();
		comboBoxN.setModel(new DefaultComboBoxModel<String>(comboName));
		comboBoxN.setBounds(169, 115, 145, 20);
		add(comboBoxN);
		Ini ini;
		try {
			ini = new Ini(new File("files\\config.ini"));
			if (ini.get("OPTIONS","language").contains("fr") && ini.get("OPTIONS","language") != null) {
				comboBoxL.setSelectedIndex(1);
			} else {
				comboBoxL.setSelectedIndex(0);
			}
			String editor=ini.get("OPTIONS","editormode");
			switch (editor) {
			case "1":
				comboBoxN.setSelectedIndex(1);
				break;
			case "2":
				comboBoxN.setSelectedIndex(2);
				break;
			case "3":
				comboBoxN.setSelectedIndex(3);
				break;
			default:
				comboBoxN.setSelectedIndex(0);
				break;
			}
		} catch (IOException e) {
			log.warn("Config.ini  (ConfigEditor) not found");
			setWarning("config.ini not found");
			e.printStackTrace();
		}
		

		JLabel lblNewLabel_2 = new JLabel("SteamApps path :");
		lblNewLabel_2.setBounds(33, 167, 137, 14);
		add(lblNewLabel_2);

		fc = new JFileChooser();
		fc.setCurrentDirectory(new File(System.getProperty("user.home")));//D:\\Steam\\steamapps
		fc.setFileSelectionMode(JFileChooser.DIRECTORIES_ONLY);

		txtWarning = new JLabel("");
		txtWarning.setEnabled(false);
		txtWarning.setForeground(Color.RED);
		txtWarning.setBounds(50, 204, 247, 14);
		add(txtWarning);

		JButton fc_btn = new JButton("Browse...");
		fc_btn.setBounds(192, 163, 89, 23);
		add(fc_btn);

		back_btn = new JButton("Cancel");
		back_btn.setBounds(50, 240, 89, 23);
		add(back_btn);

		save_btn = new JButton("Save");
		save_btn.setBounds(178, 240, 89, 23);
		add(save_btn);

		back_btn.addActionListener(this);
		fc_btn.addActionListener(this);
		save_btn.addActionListener(this);
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		if (e.getSource() == back_btn) {
			Launcheur.setPanel(new Menu());
		} else if (e.getSource() == save_btn) {
			Ini ini;
			try {
				ini = new Ini(new File("files\\config.ini"));
				ini.put("OPTIONS", "language", comboLanguage[comboBoxL.getSelectedIndex()]);
				ini.put("OPTIONS", "editormode", comboBoxN.getSelectedIndex());
				if (filepath!=null)
					ini.put("OPTIONS", "steamappspath", filepath);
				ini.store();
			} catch (IOException e1) {
				log.warn("Config.ini (ConfigEditor save_btn) not found");
				setWarning("config.ini not found");
				e1.printStackTrace();
			}
			
			Launcheur.setPanel(new Menu());
		} else {
			int option = fc.showOpenDialog(this);
			if (option == JFileChooser.APPROVE_OPTION) {
				File file = fc.getSelectedFile();
				boolean star=false;
				boolean work=false;
				for(File f:file.listFiles()) {
					
					if(f.isDirectory() && f.getName().contains("common")) {
						for(File f2:f.listFiles()) {
							if(f2.isDirectory()&&f2.getName().contains("Starbound")) {
								star=true;
								break;
							}
						}
					}else if(f.isDirectory()&&f.getName().contains("workshop")) {
						for(File f2:f.listFiles()) {
							if(f2.isDirectory()&&f2.getName().contains("content")) {
								work=true;
								break;
							}
						}
					}
					if(work && star) {
						filepath=file.getAbsolutePath();
						break;
					}
					
				}
				String alert="";
				if(work && star) {
					txtWarning.setForeground(Color.GREEN);
					setWarning("Location accepted!");
					log.info("The Steamapps path is correct. (ConfigEditor)");
				}else{
					if(!work) {
						txtWarning.setForeground(Color.RED);
						alert+="\\workshop\\content introuvable\n";
						log.error("The workshop path is not correct. (ConfigEditor)");
					}
					if(!star) {
						txtWarning.setForeground(Color.RED);
						alert+="\\common\\Starbound introuvable";
						log.error("The Starbound path is not correct. (ConfigEditor)");
					}
					setWarning(alert);
				}
			}
		}
	}

	@Override
	public void setWarning(String text) {
		txtWarning.setText(text);
		txtWarning.setVisible(true);
		txtWarning.setEnabled(true);

	}

}
