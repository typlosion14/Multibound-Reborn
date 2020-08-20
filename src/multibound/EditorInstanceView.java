package multibound;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

import javax.swing.JLabel;
import javax.swing.JList;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;

import javax.swing.SwingConstants;
import javax.swing.event.ListSelectionEvent;
import javax.swing.event.ListSelectionListener;

import org.apache.log4j.Logger;
import org.ini4j.Ini;

import javax.swing.ListSelectionModel;
import javax.swing.DefaultListModel;
import javax.swing.JButton;

import java.awt.Color;
import java.awt.Cursor;

public class EditorInstanceView extends JPanel implements ActionListener, ListSelectionListener, Panel {

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	private JButton btn_back= new JButton("ERROR"), 
			del_btn= new JButton("ERROR");
	private JLabel txtWarning = new JLabel();
	private JList<String> list = new JList<String>();
	private DefaultListModel<String> activatedModel = new DefaultListModel<String>();
	public static Logger log = Logger.getLogger(Logger.class.getName());

	@SuppressWarnings({ "rawtypes", "unchecked" })
	EditorInstanceView() {
		Launcheur.setFrame("Multibound Reborn - Choose a Instance", 100, 100, 338, 380);
		setVisible(true);
		setBounds(100, 100, 338, 380);
		JLabel title = new JLabel("Choose a Instance:");
		title.setHorizontalAlignment(SwingConstants.CENTER);
		title.setBounds(93, 22, 141, 14);
		add(title);
		setLayout(null);
		String[] listName = Instance.getListName();
		for (String element : listName) {
			activatedModel.addElement(element);
		}
		list = new JList(activatedModel);
		list.setSelectionMode(ListSelectionModel.SINGLE_INTERVAL_SELECTION);
		list.setLayoutOrientation(JList.HORIZONTAL_WRAP);
		list.setVisibleRowCount(-1);
		JScrollPane listScroller = new JScrollPane(list);
		listScroller.setSize(145, 200);
		listScroller.setLocation(90, 47);
		add(listScroller);

		btn_back = new JButton("Cancel");
		btn_back.setBounds(29, 294, 89, 23);
		add(btn_back);

		JButton ok_btn = new JButton("OK");
		ok_btn.setBounds(203, 294, 89, 23);
		add(ok_btn);

		txtWarning.setText("");
		txtWarning.setForeground(Color.RED);
		txtWarning.setBounds(11, 266, 302, 2);
		add(txtWarning);
		txtWarning.setVisible(false);
		txtWarning.setHorizontalAlignment(SwingConstants.CENTER);

		del_btn = new JButton("Delete");
		del_btn.setBounds(128, 294, 63, 23);
		add(del_btn);

		btn_back.addActionListener(this);
		ok_btn.addActionListener(this);
		list.addListSelectionListener(this);
		del_btn.addActionListener(this);
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		if (e.getSource().equals(btn_back)) {
			Launcheur.setPanel(new Menu());
		} else if (e.getSource() == del_btn) {
			int test = JOptionPane.showConfirmDialog(this,
		             "That will delete the instance and the save if you set the savelocation in Instance mode.", 
		             "Are you sure ?",
		             JOptionPane.YES_NO_OPTION);
			if (test==JOptionPane.OK_OPTION) {
				int InstanceNb = list.getSelectedIndex() + 1;
				if (list.getSelectedIndex() != -1) {
					activatedModel.remove(list.getSelectedIndex());
					list.setModel(activatedModel);
				}
				try {
					Ini ini = new Ini(new File("files\\config.ini"));
					ini.remove("INSTANCE" + InstanceNb);
					ini.store();

					String fileex = "";
					int instancenbb = InstanceNb;

					Scanner myReader = new Scanner(new File("files\\config.ini"));
					while (myReader.hasNextLine()) {
						String temp = myReader.nextLine();
						fileex += temp + "\n";
					}
					myReader.close();
					while (fileex.contains("[INSTANCE" + (instancenbb + 1))) {
						System.out.println(instancenbb + 1);
						fileex = fileex.replace("[INSTANCE" + (instancenbb + 1), "[INSTANCE" + instancenbb);
						instancenbb += 1;
					}
					FileWriter myWriter = new FileWriter("files\\config.ini");
					myWriter.write(fileex);
					myWriter.close();
				} catch (IOException e1) {
					setWarning("config.ini not found");
					log.warn("Config.ini not found (EditorInstance del_btn)");
					e1.printStackTrace();
				}
			}
		} else {
			if (list.getSelectedIndex() != -1) {
				setCursor(new Cursor(Cursor.WAIT_CURSOR));
				Launcheur.setPanel(new EditInst(list.getSelectedIndex() + 1, true));
			} else {
				txtWarning.setText("Choose a Instance");
			}
		}

	}

	@Override
	public void valueChanged(ListSelectionEvent arg0) {
		txtWarning.setVisible(false);

	}

	@Override
	public void setWarning(String text) {
		txtWarning.setVisible(true);
		txtWarning.setText(text);

	}
	
}
