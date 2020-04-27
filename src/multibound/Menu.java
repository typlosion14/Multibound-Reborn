package multibound;


import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.Font;
import java.awt.Label;

public class Menu extends JPanel implements ActionListener {
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	private JButton instance_buttonCreate,instance_buttonEdit,config_buttonClean,config_buttonEdit,other_buttonImport,other_button2;

	Menu(){
		Launcheur.setFrame("Multibound Reborn",100, 100, 450, 300);
		setVisible(true);
		setBounds(100, 100, 450, 300);

		setBorder(new EmptyBorder(5, 5, 5, 5));
		
		setLayout(null);
	
		instance_buttonCreate = new JButton("Create");
		instance_buttonCreate.setBounds(42, 111, 89, 23);
		add(instance_buttonCreate);
	
		instance_buttonEdit = new JButton("Edit");
		instance_buttonEdit.setBounds(42, 170, 89, 23);
		add(instance_buttonEdit);
	
		config_buttonClean = new JButton("Clean");
		config_buttonClean.setBounds(170, 111, 89, 23);
		add(config_buttonClean);
	
		config_buttonEdit = new JButton("Edit");
		config_buttonEdit.setBounds(170, 170, 89, 23);
		add(config_buttonEdit);
	
		other_buttonImport = new JButton("Instance");
		other_buttonImport.setBounds(310, 111, 89, 23);
		add(other_buttonImport);
	
		other_button2 = new JButton("Collection");
		other_button2.setBounds(310, 170, 89, 23);
		add(other_button2);
	
		Label instance_label = new Label("Instance");
		instance_label.setAlignment(Label.CENTER);
		instance_label.setBounds(55, 71, 62, 22);
		add(instance_label);
	
		Label config_label = new Label("Config File");
		config_label.setAlignment(Label.CENTER);
		config_label.setBounds(182, 71, 62, 22);
		add(config_label);
	
		Label other_label = new Label("Import");
		other_label.setAlignment(Label.CENTER);
		other_label.setBounds(325, 71, 62, 22);
		add(other_label);
	
		Label title = new Label("Multibound Reborn");
		title.setFont(new Font("Segoe UI", Font.BOLD, 12));
		title.setAlignment(Label.CENTER);
		title.setBounds(166, 28, 104, 22);
		add(title);
		instance_buttonCreate.addActionListener(this);
		instance_buttonEdit.addActionListener(this);
	
		config_buttonClean.addActionListener(this);
		config_buttonEdit.addActionListener(this);
	
		other_buttonImport.addActionListener(this);
		other_button2.addActionListener(this);
		System.gc();
		
	}
	@Override
	public void actionPerformed(ActionEvent e) {
		Object source=e.getSource();
		if (source==instance_buttonCreate) {
			Launcheur.setPanel(new FrameInstanceCreate());
		}else if (source==instance_buttonEdit) {
			Launcheur.setPanel(new EditorInstanceView());
		}else if (source==config_buttonClean) {
			Launcheur.setPanel(new CleanEditor());
		}else if (source==config_buttonEdit) {
			Launcheur.setPanel(new ConfigEditor());
		}else if (source==other_buttonImport) {
			Launcheur.setPanel(new ImportInstance());
		}else {
			Launcheur.setPanel(new ImportCollectionSteam());
		}
		
	}
	
	

}
