package multibound;

import java.awt.Cursor;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.util.Arrays;

import javax.swing.DefaultListModel;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JLabel;
import javax.swing.JList;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextField;
import javax.swing.SwingConstants;
import javax.swing.event.ListSelectionEvent;
import javax.swing.event.ListSelectionListener;

import org.apache.log4j.Logger;
import org.ini4j.Ini;

public class EditInst extends JPanel implements ActionListener, ListSelectionListener, Panel {

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	private Instance instance;
	public JLabel warningText = new JLabel();
	private JList<Mods> disabledList, 
						activatedList;
	private JButton save_btn = new JButton("ERROR"), 
			back_btn = new JButton("ERROR"), 
			doubleArrow = new JButton("ERROR"),
			DisabledBtn = new JButton("ERROR"), 
			ActivatedBtn = new JButton("ERROR"),
			btnAllDisabled = new JButton("ERROR"), 
			btnAllActived = new JButton("ERROR");
	private JTextField txtGetname = new JTextField();
	private boolean isWorkshop;
	private String[] combolist = { "default", "Instance" };
	private JComboBox<String> comboBox;
	public static Logger log = Logger.getLogger(Logger.class.getName());

	EditInst(int INb, boolean a) {
		isWorkshop = a;
		log.info("Loading Instance "+INb+" (EditInst)");
		instance = new Instance(INb);
		log.info("Loaded Instance "+INb+" (EditInst)");
		if (isWorkshop) {
			Launcheur.setFrame("Multibound Reborn - Edit Workshop " + instance.getName(), 100, 100, 586, 404);
			setBounds(100, 100, 586, 404);
		} else {
			Launcheur.setFrame("Multibound Reborn - Edit Mods " + instance.getName(), 100, 100, 586, 405);
			setBounds(100, 100, 586, 405);
		}

		setLayout(null);

		JLabel lblName = new JLabel("Name :");
		lblName.setHorizontalAlignment(SwingConstants.CENTER);
		lblName.setBounds(96, 11, 46, 14);
		add(lblName);

		txtGetname.setText(instance.getName());
		txtGetname.setBounds(152, 8, 86, 20);
		add(txtGetname);
		txtGetname.setColumns(10);

		JLabel lblSave = new JLabel("Save Location :");
		lblSave.setBounds(291, 11, 78, 14);
		add(lblSave);

		comboBox = new JComboBox<String>(combolist);
		if (!instance.getSaveLocation().equals("default") && instance.getSaveLocation()!=null) {
			comboBox.setSelectedIndex(1);
		} else {
			comboBox.setSelectedIndex(0);
		}

		comboBox.setBounds(390, 8, 67, 20);
		add(comboBox);
		
		if (isWorkshop) {
			log.info("Loading Workshop List (EditInst)");
			disabledList = new JList<Mods>(instance.getDesactivedWorskshop(warningText));
			activatedList = new JList<Mods>(instance.getWorkshopList());
			log.info("Loaded Workshop List (EditInst)");
		} else {
			log.info("Loading Mods List (EditInst)");
			disabledList = new JList<Mods>(instance.getDesactivedMods(warningText));
			activatedList = new JList<Mods>(instance.getModsList());
			log.info("Loaded Mods List (EditInst)");
		}
		setCursor(new Cursor(Cursor.DEFAULT_CURSOR));
		disabledList.setLayoutOrientation(JList.HORIZONTAL_WRAP);
		disabledList.setVisibleRowCount(-1);
		JScrollPane listScroller = new JScrollPane(disabledList);
		listScroller.setSize(145, 210);
		listScroller.setLocation(106, 80);
		add(listScroller);

		save_btn = new JButton("Save");
		save_btn.setBounds(345, 313, 89, 23);
		add(save_btn);

		activatedList.setLayoutOrientation(JList.HORIZONTAL_WRAP);
		activatedList.setVisibleRowCount(-1);

		JScrollPane listScroller_1 = new JScrollPane(activatedList);
		listScroller_1.setBounds(321, 80, 145, 210);
		add(listScroller_1);

		back_btn = new JButton("Cancel");
		back_btn.setBounds(129, 313, 89, 23);
		add(back_btn);

		JLabel DLabel = new JLabel("Disabled");
		DLabel.setHorizontalAlignment(SwingConstants.CENTER);
		DLabel.setBounds(152, 55, 46, 14);
		add(DLabel);

		JLabel ActLabel = new JLabel("Activated");
		ActLabel.setHorizontalAlignment(SwingConstants.CENTER);
		ActLabel.setBounds(365, 55, 54, 14);
		add(ActLabel);

		doubleArrow = new JButton("<->");
		doubleArrow.setBounds(261, 119, 54, 23);
		add(doubleArrow);

		ActivatedBtn = new JButton("->");
		ActivatedBtn.setBounds(264, 175, 47, 23);
		add(ActivatedBtn);

		DisabledBtn = new JButton("<-");
		DisabledBtn.setBounds(264, 231, 47, 23);
		add(DisabledBtn);

		btnAllDisabled = new JButton("All Disabled");
		btnAllDisabled.setBounds(7, 175, 89, 23);
		add(btnAllDisabled);

		btnAllActived = new JButton("All Actived");
		btnAllActived.setBounds(476, 175, 89, 23);
		add(btnAllActived);

		warningText.setVisible(false);
		warningText.setBounds(106, 34, 360, 20);
		add(warningText);

		back_btn.addActionListener(this);
		save_btn.addActionListener(this);
		ActivatedBtn.addActionListener(this);
		DisabledBtn.addActionListener(this);
		doubleArrow.addActionListener(this);
		btnAllDisabled.addActionListener(this);
		btnAllActived.addActionListener(this);

		disabledList.addListSelectionListener(this);
		activatedList.addListSelectionListener(this);
	}


	@Override
	public void valueChanged(ListSelectionEvent e) {
		warningText.setVisible(false);

	}

	@Override
	public void actionPerformed(ActionEvent e) {
		Object source = e.getSource();
		if (source.equals(back_btn)) {
			if (isWorkshop) {
				Launcheur.setPanel(new Menu());
			} else {
				
				Launcheur.setPanel(new EditInst(instance.getNumber(), true));
			}

		} else if (source.equals(save_btn)) {
			if (txtGetname.getText().length() != 0) {
				try {
					Ini ini = new Ini(new File("files\\config.ini"));
					ini.put("INSTANCE" + instance.getNumber(), "name",
							txtGetname.getText().replace("[INSTANCE", "Instance"));
					String saveloc = ini.get("INSTANCE" + instance.getNumber(), "savelocation");
					ini.put("INSTANCE" + instance.getNumber(), "savelocation", combolist[comboBox.getSelectedIndex()]);
					if (!saveloc.equals(combolist[comboBox.getSelectedIndex()])
							&& combolist[comboBox.getSelectedIndex()].equals("default")) {
						String steampath = ini.get("OPTIONS", "steamappspath");
						for (File f : new File(steampath + "\\common\\Starbound\\InstanceSave\\" + instance.getNumber())
								.listFiles()) {
							if (f.isDirectory()) {
								for (File f2 : f.listFiles()) {
									Files.move(f2.toPath(), new File(steampath + "\\common\\Starbound\\storage\\"
											+ f.getName() + "\\" + f2.getName()).toPath());
								}

							}
						}
					}
					Mods[] tempA = getAllElements(activatedList);
					if (tempA.length != 0) {
						String totalA = tempA[0].getFilename();
						for (int i = 1; i < tempA.length; i++) {
							totalA += "," + tempA[i].getFilename();
						}
						if (isWorkshop) {
							ini.put("INSTANCE" + instance.getNumber(), "workshoplist", totalA);
						} else {
							ini.put("INSTANCE" + instance.getNumber(), "modslist", totalA);
						}
					} else {
						if (isWorkshop) {
							ini.put("INSTANCE" + instance.getNumber(), "workshoplist", "None");
						} else {
							ini.put("INSTANCE" + instance.getNumber(), "modslist", "None");
						}
					}
					ini.store();
				} catch (IOException e1) {
					setWarning("config.ini not found");
					log.warn("Config.ini not found (EditInst save_btn)");
					e1.printStackTrace();
				}
				if (isWorkshop) {
					Launcheur.setPanel(new EditInst(instance.getNumber(), false));
				} else {
					Launcheur.setPanel(new Menu());
				}
			} else {
				setWarning("Enter a name");
			}

		} else if (source.equals(btnAllActived)) {
			Mods[] tempD = getAllElements(disabledList);
			Mods[] tempA = getAllElements(activatedList);
			DefaultListModel<Mods> activatedModel = new DefaultListModel<Mods>();
			for (Mods element : tempD) {
				activatedModel.addElement(element);
			}
			for (Mods element : tempA) {
				activatedModel.addElement(element);
			}
			activatedList.setModel(activatedModel);
			disabledList.setModel(new DefaultListModel<Mods>());

		} else if (source.equals(btnAllDisabled)) {
			Mods[] tempD = getAllElements(disabledList);
			Mods[] tempA = getAllElements(activatedList);
			DefaultListModel<Mods> disabledModel = new DefaultListModel<Mods>();
			for (Mods element : tempD) {
				disabledModel.addElement(element);
			}
			for (Mods element : tempA) {
				disabledModel.addElement(element);
			}
			activatedList.setModel(new DefaultListModel<Mods>());
			disabledList.setModel(disabledModel);

		} else if (source.equals(ActivatedBtn) && !disabledList.isSelectionEmpty()) {

			int[] select = disabledList.getSelectedIndices();
			// New DesactivedList
			Mods[] temp = getAllElements(disabledList);
			DefaultListModel<Mods> disabledModel = new DefaultListModel<Mods>();
			for (Mods element : temp) {
				disabledModel.addElement(element);
			}
			for (int i = 0; i < select.length; i++) {
				disabledModel.removeElement(temp[select[i]]);
			}

			// New ActivatedList
			temp = getAllElements(activatedList);
			DefaultListModel<Mods> activatedModel = new DefaultListModel<Mods>();
			for (int i = 0; i < select.length; i++) {
				activatedModel.addElement(disabledList.getModel().getElementAt(select[i]));
			}

			for (Mods element : temp) {
				activatedModel.addElement(element);
			}
			// Set Model
			activatedList.setModel(activatedModel);
			disabledList.setModel(disabledModel);
		} else if (source.equals(DisabledBtn) && !activatedList.isSelectionEmpty()) {
			int[] select = activatedList.getSelectedIndices();
			// New DesactivedList
			Mods[] temp = getAllElements(activatedList);
			DefaultListModel<Mods> activatedModel = new DefaultListModel<Mods>();
			for (Mods element : temp) {
				activatedModel.addElement(element);
			}
			for (int i = 0; i < select.length; i++) {
				activatedModel.removeElement(temp[select[i]]);
			}

			// New ActivatedList
			temp = getAllElements(disabledList);
			DefaultListModel<Mods> disabledModel = new DefaultListModel<Mods>();
			for (int i = 0; i < select.length; i++) {
				disabledModel.addElement(activatedList.getModel().getElementAt(select[i]));
			}

			for (Mods element : temp) {
				disabledModel.addElement(element);
			}
			// Set Model
			activatedList.setModel(activatedModel);
			disabledList.setModel(disabledModel);
		} else if (disabledList.isSelectionEmpty() && activatedList.isSelectionEmpty()) {
			setWarning("Choose mods in one of the list");
		} else if (source.equals(doubleArrow) && !disabledList.isSelectionEmpty()
				&& !activatedList.isSelectionEmpty()) {
			int[] selectA = activatedList.getSelectedIndices();
			int[] selectD = disabledList.getSelectedIndices();
			Mods[] ElementsD = getAllElements(disabledList);
			Mods[] ElementsA = getAllElements(activatedList);

			DefaultListModel<Mods> disabledModel = new DefaultListModel<Mods>();
			DefaultListModel<Mods> activatedModel = new DefaultListModel<Mods>();

			for (Mods element : ElementsA) {
				activatedModel.addElement(element);
			}

			for (Mods element : ElementsD) {
				disabledModel.addElement(element);
			}
			for (int i = 0; i < selectD.length; i++) {
				disabledModel.removeElement(ElementsD[selectD[i]]);
				activatedModel.addElement(ElementsD[selectD[i]]);
			}
			for (int i = 0; i < selectA.length; i++) {
				disabledModel.addElement(ElementsA[selectA[i]]);
				activatedModel.removeElement(ElementsA[selectA[i]]);
			}

			activatedList.setModel(activatedModel);
			disabledList.setModel(disabledModel);

		}
		Mods[] ElementsD = getAllElements(disabledList);
		Mods[] ElementsA = getAllElements(activatedList);
		Arrays.sort(ElementsD);
		Arrays.sort(ElementsA);
		DefaultListModel<Mods> disabledModel = new DefaultListModel<Mods>();
		DefaultListModel<Mods> activatedModel = new DefaultListModel<Mods>();
		for (int i = 0; i < ElementsD.length; i++) {
			disabledModel.addElement(ElementsD[i]);
		}
		for (int i = 0; i < ElementsA.length; i++) {
			activatedModel.addElement(ElementsA[i]);
		}
		activatedList.setModel(activatedModel);
		disabledList.setModel(disabledModel);

	}

	@Override
	public void setWarning(String text) {
		warningText.setText(text);
		warningText.setVisible(true);

	}

	public static Mods[] getAllElements(JList<Mods> list) {
		Mods[] r = new Mods[list.getModel().getSize()];
		for (int i = 0; i < list.getModel().getSize(); i++) {
			r[i] = list.getModel().getElementAt(i);
		}
		return r;
	}

}
