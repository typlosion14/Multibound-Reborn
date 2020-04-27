package multibound;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JList;
import javax.swing.JScrollPane;
import javax.swing.SwingConstants;
import javax.swing.JTextField;
import javax.swing.ListSelectionModel;
import javax.swing.JSpinner;
import javax.swing.SpinnerListModel;
import javax.swing.JComboBox;
import javax.swing.JFileChooser;
import javax.swing.JButton;
import java.awt.Component;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import javax.swing.DefaultComboBoxModel;
import java.awt.Color;

public class test {

	private JFrame frame;
	private JTextField warningText;
	private JTextField name_field;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					test window = new test();
					window.frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the application.
	 */
	public test() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frame = new JFrame();
		frame.setBounds(100, 100, 361, 342);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.getContentPane().setLayout(null);
		
		JLabel title = new JLabel("Instance Import");
		title.setHorizontalAlignment(SwingConstants.CENTER);
		title.setBounds(107, 11, 108, 14);
		frame.getContentPane().add(title);
		
		JFileChooser fc = new JFileChooser();
		fc.setBounds(262, 167, -92, 14);
		frame.getContentPane().add(fc);
		
		JLabel txtWarning = new JLabel("");
		txtWarning.setEnabled(false);
		txtWarning.setForeground(Color.RED);
		txtWarning.setBounds(50, 204, 247, 14);
		frame.getContentPane().add(txtWarning);
		
		JButton back_btn = new JButton("Cancel");
		back_btn.setBounds(50, 240, 89, 23);
		frame.getContentPane().add(back_btn);
		
		JButton save_btn = new JButton("Import");
		save_btn.setBounds(178, 240, 89, 23);
		frame.getContentPane().add(save_btn);
		
		JLabel name_label = new JLabel("Name:");
		name_label.setHorizontalAlignment(SwingConstants.CENTER);
		name_label.setBounds(70, 54, 46, 14);
		frame.getContentPane().add(name_label);
		
		name_field = new JTextField();
		name_field.setBounds(181, 51, 86, 20);
		frame.getContentPane().add(name_field);
		name_field.setColumns(10);
		
		JLabel saveloca_label = new JLabel("Save Location:");
		saveloca_label.setHorizontalAlignment(SwingConstants.CENTER);
		saveloca_label.setBounds(50, 95, 86, 14);
		frame.getContentPane().add(saveloca_label);
		
		JComboBox comboBox = new JComboBox();
		comboBox.setModel(new DefaultComboBoxModel(new String[] {"default", "Instance"}));
		comboBox.setBounds(182, 93, 86, 20);
		frame.getContentPane().add(comboBox);
		
		JLabel import_label = new JLabel("Collection URL:");
		import_label.setHorizontalAlignment(SwingConstants.CENTER);
		import_label.setBounds(50, 138, 89, 14);
		frame.getContentPane().add(import_label);
		
		JTextField collectionField = new JTextField("");
		collectionField.setBounds(178, 134, 89, 23);
		frame.getContentPane().add(collectionField);
		
		JButton btnNewButton = new JButton("Check");
		btnNewButton.setBounds(110, 167, 89, 23);
		frame.getContentPane().add(btnNewButton);
		
		

	}
}
