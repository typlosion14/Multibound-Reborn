package multibound;

import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.IOException;
import java.util.regex.Pattern;

import javax.swing.DefaultComboBoxModel;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.SwingConstants;

import org.ini4j.Ini;

public class ImportCollectionSteam extends JPanel implements Panel, ActionListener {
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	JLabel txtWarning;
	JButton back_btn, save_btn, check_btn;
	JTextField name_field, collectionField;
	String[] workshopList = null, comboS = new String[] { "default", "Instance" };
	JComboBox<String> comboBox;

	public ImportCollectionSteam() {
		setBounds(100, 100, 361, 342);
		Launcheur.setFrame("Multibound Reborn - Collection Import", 100, 100, 361, 342);
		JLabel title = new JLabel("Collection Import");
		setLayout(null);
		title.setHorizontalAlignment(SwingConstants.CENTER);
		title.setBounds(107, 11, 108, 14);
		add(title);

		txtWarning = new JLabel("");
		txtWarning.setVisible(false);
		txtWarning.setForeground(Color.RED);
		txtWarning.setBounds(50, 204, 247, 14);
		add(txtWarning);

		back_btn = new JButton("Cancel");
		back_btn.setBounds(50, 240, 89, 23);
		add(back_btn);

		save_btn = new JButton("Import");
		save_btn.setBounds(178, 240, 89, 23);
		add(save_btn);

		JLabel name_label = new JLabel("Name:");
		name_label.setHorizontalAlignment(SwingConstants.CENTER);
		name_label.setBounds(70, 54, 46, 14);
		add(name_label);

		name_field = new JTextField();
		name_field.setBounds(181, 51, 86, 20);
		add(name_field);
		name_field.setColumns(10);

		JLabel saveloca_label = new JLabel("Save Location:");
		saveloca_label.setHorizontalAlignment(SwingConstants.CENTER);
		saveloca_label.setBounds(50, 95, 86, 14);
		add(saveloca_label);

		comboBox = new JComboBox<String>();
		comboBox.setModel(new DefaultComboBoxModel<String>(comboS));
		comboBox.setBounds(182, 93, 86, 20);
		add(comboBox);

		JLabel import_label = new JLabel("Collection URL:");
		import_label.setHorizontalAlignment(SwingConstants.CENTER);
		import_label.setBounds(50, 138, 89, 14);
		add(import_label);

		collectionField = new JTextField("");
		collectionField.setBounds(178, 134, 89, 23);
		add(collectionField);

		check_btn = new JButton("Check");
		check_btn.setBounds(110, 167, 89, 23);
		add(check_btn);

		back_btn.addActionListener(this);
		save_btn.addActionListener(this);
		check_btn.addActionListener(this);
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		Object source = e.getSource();
		if (source == back_btn) {
			Launcheur.setPanel(new Menu());
		} else if (source == save_btn) {
			if (check()) {
					String workshopL = workshopList[0];
					for (int i = 1; i < workshopList.length; i++)
						workshopL += "," + workshopList[i];
					Ini ini;
					try {
						ini = new Ini(new File("files\\config.ini"));
						int i = 1;
						while (ini.get("INSTANCE" + i, "name") != null) {
							i++;
						}
						ini.put("INSTANCE" + i, "name", name_field.getText().replace("[INSTANCE", "Instance"));
						ini.put("INSTANCE" + i, "savelocation", comboS[comboBox.getSelectedIndex()]);
						ini.put("INSTANCE" + i, "workshoplist", workshopL);
						ini.put("INSTANCE" + i, "modslist", "None");
						ini.store();
					} catch (IOException e1) {
						// TODO Auto-generated catch block
						e1.printStackTrace();
					}
					
				}
		} else {check();}

	}

	@Override
	public void setWarning(String text) {
		txtWarning.setText(text);
		txtWarning.setVisible(true);
		txtWarning.setEnabled(true);

	}

	static public String[] getWorkshopIdFromCollection(String url) {
		try {
			String html = Mods.getHtml(url);
			int countMods = (html.split(Pattern.quote("\"id\":\""), -1).length) - 1;
			String[] WorkshopList = new String[countMods];
			int pos = 0;
			for (int i = 0; i < countMods; i++) {
				pos = html.indexOf("\"id\":\"", pos + "\"id\":\"".length() + 1);
				WorkshopList[i] = html.substring(pos + "\"id\":\"".length(),
						html.indexOf("\"", pos + "\"id\":\"".length() + 1));
			}
			return WorkshopList;
		} catch (Exception e) {
			return null;
		}

	}
	public boolean check() {
		if (collectionField.getText() != null && collectionField.getText().length() > 0) {
			String html = Mods.getHtml(collectionField.getText());
			int pos1=html.indexOf("content=\"Steam Workshop: ")+"content=\"Steam Workshop: ".length();
			String content=html.substring(pos1,html.indexOf(". ", pos1));
			if(content.contains("Starbound")) {
				workshopList = getWorkshopIdFromCollection(collectionField.getText());
				if (workshopList == null) {
					txtWarning.setForeground(Color.RED);
					setWarning("Collection can't be Import.");
					return false;
				} else {
					txtWarning.setForeground(Color.GREEN);
					setWarning("Collection can be Import.");
					return true;
				}
			}else {
				txtWarning.setForeground(Color.RED);
				setWarning("Enter a Starbound collection URL pls.");
				return false;
			}
		} else {
			txtWarning.setForeground(Color.RED);
			setWarning("Enter a collection URL pls.");
			return false;
		}
	}
}
