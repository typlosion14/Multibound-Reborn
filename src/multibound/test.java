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
		frame.setBounds(100, 100, 361, 175);
		frame.getContentPane().setBounds(100, 100, 361, 175);
		frame.getContentPane().setLayout(null);

		JLabel title = new JLabel("Clean files");
		title.setHorizontalAlignment(SwingConstants.CENTER);
		title.setBounds(119, 11, 108, 14);
		frame.getContentPane().add(title);

		JLabel warning_label = new JLabel("You're about to clean files mods.");
		warning_label.setHorizontalAlignment(SwingConstants.CENTER);
		warning_label.setBounds(36, 36, 274, 25);
		frame.getContentPane().add(warning_label);

		JLabel label_1 = new JLabel(" if you want uninstall Multibound Reborn it's imperative.");
		label_1.setHorizontalAlignment(SwingConstants.CENTER);
		label_1.setBounds(24, 64, 285, 14);
		frame.getContentPane().add(label_1);

		JButton back_btn = new JButton("Cancel");
		back_btn.setBounds(36, 91, 89, 23);
		frame.getContentPane().add(back_btn);

		JButton clean_btn = new JButton("Mods");
		clean_btn.setBounds(221, 91, 89, 23);
		frame.getContentPane().add(clean_btn);
		
		JButton clean_btn_1 = new JButton("Save");
		clean_btn_1.setBounds(129, 91, 89, 23);
		frame.getContentPane().add(clean_btn_1);

		
		
		
		

	}
}
