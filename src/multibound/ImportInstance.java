package multibound;

import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

import javax.swing.DefaultComboBoxModel;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JFileChooser;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.SwingConstants;
import javax.swing.filechooser.FileNameExtensionFilter;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

public class ImportInstance extends JPanel implements Panel, ActionListener {
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	private JLabel txtWarning= new JLabel("");
	private JFileChooser fc=new JFileChooser();
	private JButton fc_btn= new JButton("ERROR"),
		back_btn= new JButton("ERROR"),
		save_btn= new JButton("ERROR");
	private JTextField name_field= new JTextField();
	boolean fileAccepted = false;
	private File file = null;

	public ImportInstance() {
		setBounds(100, 100, 361, 342);
		Launcheur.setFrame("Multibound Reborn - Instance Import", 100, 100, 361, 342);
		JLabel title = new JLabel("Instance Import");
		title.setHorizontalAlignment(SwingConstants.CENTER);
		setLayout(null);
		title.setBounds(107, 11, 108, 14);
		add(title);

		txtWarning.setEnabled(false);
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
		name_label.setBounds(75, 54, 46, 14);
		add(name_label);

		name_field.setBounds(181, 51, 86, 20);
		add(name_field);
		name_field.setColumns(10);

		JLabel saveloca_label = new JLabel("Save Location:");
		saveloca_label.setHorizontalAlignment(SwingConstants.CENTER);
		saveloca_label.setBounds(53, 115, 86, 14);
		add(saveloca_label);

		JComboBox<String> comboBox = new JComboBox<String>();
		comboBox.setModel(new DefaultComboBoxModel<String>(new String[] { "default", "Instance" }));
		comboBox.setBounds(181, 112, 86, 20);
		add(comboBox);

		JLabel import_label = new JLabel("Import :");
		import_label.setHorizontalAlignment(SwingConstants.CENTER);
		import_label.setBounds(75, 167, 46, 14);
		add(import_label);

		fc.setCurrentDirectory(new File("D:\\Cours\\HS\\MultiBound-master\\ExampleRoot\\instances\\Modpack Example"));
		fc.setFileFilter(new FileNameExtensionFilter("JSON", "json"));
		fc.setFileSelectionMode(JFileChooser.FILES_ONLY);

		fc_btn = new JButton("Browse...");
		fc_btn.setBounds(179, 164, 89, 23);
		add(fc_btn);

		back_btn.addActionListener(this);
		fc_btn.addActionListener(this);
		save_btn.addActionListener(this);
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		Object source = e.getSource();
		if (source.equals(back_btn)) {
			Launcheur.setPanel(new Menu());
		} else if (source.equals(save_btn)) {
			if (file != null && fileAccepted) {
				JSONParser parser = new JSONParser();
				try {

					Scanner myReader = new Scanner(file);
					String jsonfile = "";
					while (myReader.hasNextLine()) {
						String tempStr = myReader.nextLine();
						if (tempStr.contains("//")) {
							int pos1 = tempStr.indexOf("//");
							String comment = tempStr.substring(pos1);
							jsonfile += tempStr.replace(comment, "");
						} else {
							jsonfile += tempStr;
						}
					}
					myReader.close();
					JSONObject jsonObject = (JSONObject) parser.parse(jsonfile);
					JSONArray assets = (JSONArray) jsonObject.get("assetSources");
					JSONObject temp = (JSONObject) assets.get(0);
					if (temp.get("blacklist") == null) {
						// TODO finish blacklist Import JSONArray
					} else {
						System.out.println(temp.get("blacklist"));
						JSONArray blacklist = (JSONArray) temp.get("blacklist");
						String[] idblack = new String[blacklist.size()];
						ArrayList<String> arrayblack = new ArrayList<String>();
						ArrayList<String> arrayworkshop = new ArrayList<String>();
						Mods[] workshoplist = Instance.getWorkshopFile(txtWarning);
						for (int i = 0; i < workshoplist.length; i++) {
							arrayworkshop.add(Integer.toString(workshoplist[i].getId()));
						}
						for (int i = 0; i < blacklist.size(); i++) {
							if (Integer.parseInt((String) blacklist.get(i)) > 0) {
								arrayblack.add((String) blacklist.get(i));
							}
						}
						// TODO finish blacklsit de mort
						arrayblack.toArray(idblack);

					}
				} catch (Exception E) {
					E.printStackTrace();
				}

			}
		} else {
			int option = fc.showOpenDialog(this);
			if (option == JFileChooser.APPROVE_OPTION) {
				file = fc.getSelectedFile();
				JSONParser parser = new JSONParser();
				try {

					Scanner myReader = new Scanner(file);
					String jsonfile = "";
					while (myReader.hasNextLine()) {
						String tempStr = myReader.nextLine();
						if (tempStr.contains("//")) {
							int pos1 = tempStr.indexOf("//");
							String comment = tempStr.substring(pos1);
							jsonfile += tempStr.replace(comment, "");
						} else {
							jsonfile += tempStr;
						}

					}
					myReader.close();
					JSONObject jsonObject = (JSONObject) parser.parse(jsonfile);
					JSONObject info = (JSONObject) jsonObject.get("info");
					if (name_field.getText().length() == 0) {
						name_field.setText((String) info.get("name"));
					}
					JSONArray assets = (JSONArray) jsonObject.get("assetSources");
					JSONObject temp = (JSONObject) assets.get(0);
					fileAccepted = true;
					if (temp != null) {
						if (assets != null && temp != null && temp.get("blacklist") == null
								&& temp.get("workshopId") == null && temp.get("id") == null) {
							fileAccepted = false;
							txtWarning.setForeground(Color.RED);
							setWarning("This file can't be loaded as a Instance");
						}
					} else {

						fileAccepted = false;
						txtWarning.setForeground(Color.RED);
						setWarning("This file can't be loaded as a Instance");
					}
					if (fileAccepted) {
						txtWarning.setForeground(Color.GREEN);
						setWarning("This file can be loaded as a Instance");
					}

				} catch (IOException er) {
					er.printStackTrace();
				} catch (ParseException er) {
					er.printStackTrace();
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
