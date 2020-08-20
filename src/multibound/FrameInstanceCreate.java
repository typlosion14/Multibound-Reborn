package multibound;

import javax.swing.JPanel;
import javax.swing.JLabel;
import javax.swing.SwingConstants;

import org.apache.log4j.Logger;
import org.ini4j.Ini;

import javax.swing.JTextField;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.IOException;

import javax.swing.JButton;
import java.awt.Color;

public class FrameInstanceCreate extends JPanel implements ActionListener,Panel {

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	private JTextField textField;
	private JButton btn_yes;
	private JButton btn_back;
	private JLabel txtWarning = new JLabel("");
	public static Logger log = Logger.getLogger(Logger.class.getName());

	/**
	 * Create the frame.
	 */
	public FrameInstanceCreate() {
		Launcheur.setFrame("Multibound Reborn - Create Instance",100, 100, 213, 211);
		setBounds(100, 100, 213, 211);
		setLayout(null);
		
		JLabel title = new JLabel("Create Your New Instance");
		title.setHorizontalAlignment(SwingConstants.CENTER);
		title.setBounds(24, 11, 141, 14);
		add(title);
		
		JLabel label_name = new JLabel("Name:");
		label_name.setHorizontalAlignment(SwingConstants.CENTER);
		label_name.setBounds(72, 36, 46, 14);
		add(label_name);
		
		textField = new JTextField();
		textField.setToolTipText("");
		textField.setBounds(52, 58, 86, 20);
		add(textField);
		textField.setColumns(10);
		
		btn_yes = new JButton("Accept");
		btn_yes.setBounds(100, 135, 89, 23);
		add(btn_yes);
		
		btn_back = new JButton("Back");
		btn_back.setBounds(10, 135, 79, 23);
		add(btn_back);
		
		btn_back.addActionListener(this);
		btn_yes.addActionListener(this);
		txtWarning.setForeground(Color.RED);
		
		
		txtWarning.setBounds(24, 99, 165, 14);
		add(txtWarning);
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		Object source=e.getSource();
		if(source.equals(btn_back)) {
			Launcheur.setPanel(new Menu());
		}else if(source.equals(btn_yes)){
			if(textField.getText().length()!=0) {
	            Ini ini;
				try {
					ini = new Ini(new File("files\\config.ini"));
		            int i=1;
		            while(ini.get("INSTANCE"+i,"name")!=null) {
		            	i++;
		            }
		            ini.put("INSTANCE"+i,"name",textField.getText());
		            ini.put("INSTANCE"+i,"workshoplist","None");
		            ini.put("INSTANCE"+i,"modslist","None");
		            ini.put("INSTANCE"+i,"savelocation","default");
		            ini.store();
		            log.info("Create the Instance "+textField.getText());
		            Launcheur.setPanel(new EditInst(i,true));
				} catch (IOException e1) {
					setWarning("config.ini not found");
					log.warn("Config.ini not found (FrameInstanceCreate btn_yes)");
					e1.printStackTrace();
				}
			}else {
				setWarning("Enter a name");
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
