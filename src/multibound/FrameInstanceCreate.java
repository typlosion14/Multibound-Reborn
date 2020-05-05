package multibound;

import javax.swing.JPanel;
import javax.swing.JLabel;
import javax.swing.SwingConstants;

import org.ini4j.Ini;

import javax.swing.JTextField;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;

import javax.swing.JButton;

public class FrameInstanceCreate extends JPanel implements ActionListener {

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	private JTextField textField;
	private JButton btn_yes;
	private JButton btn_back;

	/**
	 * Create the frame.
	 */
	public FrameInstanceCreate() {
		Launcheur.setFrame("Multibound Reborn - Create Instance",100, 100, 213, 169);
		setBounds(100, 100, 213, 169);
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
		btn_yes.setBounds(98, 92, 89, 23);
		add(btn_yes);
		
		btn_back = new JButton("Back");
		btn_back.setBounds(9, 92, 79, 23);
		add(btn_back);
		
		btn_back.addActionListener(this);
		btn_yes.addActionListener(this);
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		Object source=e.getSource();
		if(source.equals(btn_back)) {
			Launcheur.setPanel(new Menu());
		}else if(source.equals(btn_yes)){
			if(textField.getText().length()!=0) {
				try{
		            Ini ini = new Ini(new File("files\\config.ini"));
		            int i=1;
		            while(ini.get("INSTANCE"+i,"name")!=null) {
		            	i++;
		            }
		            ini.put("INSTANCE"+i,"name",textField.getText());
		            ini.put("INSTANCE"+i,"workshoplist","None");
		            ini.put("INSTANCE"+i,"modslist","None");
		            ini.put("INSTANCE"+i,"savelocation","default");
		            ini.store();
		            Launcheur.setPanel(new EditInst(i,true));
		        }catch(Exception er){
		            System.err.println(er.getMessage());
		        }
			}else {
				//TODO Warning
			}
			
		}
		
	}
}
