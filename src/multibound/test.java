package multibound;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JLabel;

import javax.swing.SwingConstants;

import javax.swing.JProgressBar;

import java.awt.FlowLayout;


public class test {

	private JFrame frame;

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
		frame.setBounds(100, 100, 310, 101);
		frame.getContentPane().setBounds(100, 100, 361, 175);
				frame.getContentPane().setLayout(new FlowLayout(FlowLayout.CENTER, 5, 5));
		
				JLabel title = new JLabel("Clean files");
				title.setHorizontalAlignment(SwingConstants.CENTER);
				frame.getContentPane().add(title);
		
		JProgressBar progressBar = new JProgressBar();
		frame.getContentPane().add(progressBar);

		
		
		
		

	}
}
