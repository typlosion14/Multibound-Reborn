package multibound;


import javax.swing.JFrame;
import javax.swing.JPanel;




public class Launcheur{

	static JPanel panel;
	static JFrame frame;

	public static void main(String[] args) {
		// Initialisation
		
		// Menu
		frame=new JFrame();
		panel=new Menu();
		frame.setVisible(true);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setContentPane(panel);
		/*frame.addComponentListener(new ComponentAdapter() 
		{  
		        public void componentResized(ComponentEvent evt) {
		            Component c = (Component)evt.getSource();
		            System.out.println(c);
		        }
		});*///TODO Resize dynamic
		
		
	}

	public static void setPanel(JPanel panel) {
		frame.setContentPane(panel);
	}
	
	public static void setFrame(String title, int x,int y,int width,int height) {
		frame.setTitle(title);
		frame.setBounds(x, y, width, height);
	}
	
	public static JFrame getFrame() {
		return frame;
	}
	//TODO Language

	
}
