package multibound;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JLabel;
import javax.swing.JList;
import javax.swing.JPanel;
import javax.swing.JScrollPane;

import javax.swing.SwingConstants;
import javax.swing.event.ListSelectionEvent;
import javax.swing.event.ListSelectionListener;
import javax.swing.JTextField;
import javax.swing.ListSelectionModel;
import javax.swing.JButton;
import java.awt.Color;

public class EditorInstanceView extends JPanel implements ActionListener, ListSelectionListener,Panel  {

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	JButton btn_back,ok_btn;
	private JTextField txtWarning;
	JList<String> list;
	
	@SuppressWarnings({ "rawtypes", "unchecked" })
	EditorInstanceView(){
		Launcheur.setFrame("Multibound Reborn - Choose a Instance",100, 100, 338, 380);
		setVisible(true);
		setBounds(100, 100, 338, 380);
		JLabel title = new JLabel("Choose a Instance:");
		title.setHorizontalAlignment(SwingConstants.CENTER);
		title.setBounds(93, 22, 141, 14);
		add(title);
		setLayout(null);
		
		list = new JList(Instance.getListName()); 
		list.setSelectionMode(ListSelectionModel.SINGLE_INTERVAL_SELECTION);
		list.setLayoutOrientation(JList.HORIZONTAL_WRAP);
		list.setVisibleRowCount(-1);
		JScrollPane listScroller = new JScrollPane(list);
		listScroller.setSize(145, 200);
		listScroller.setLocation(93, 60);
		add(listScroller);
		
		//TODO Add a delete button
		
		btn_back = new JButton("Cancel");
		btn_back.setBounds(49, 295, 89, 23);
		add(btn_back);
		
		ok_btn = new JButton("OK");
		ok_btn.setBounds(195, 295, 89, 23);
		add(ok_btn);
		
		txtWarning = new JTextField();
		txtWarning.setText("");
		txtWarning.setForeground(Color.RED);
		txtWarning.setEditable(false);
		txtWarning.setBounds(10, 271, 302, 20);
		add(txtWarning);
		txtWarning.setColumns(10);
		txtWarning.setVisible(false);
		txtWarning.setHorizontalAlignment(SwingConstants.CENTER);
		
		btn_back.addActionListener(this);
		ok_btn.addActionListener(this);
		list.addListSelectionListener(this);
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		if(e.getSource()==btn_back) {
			Launcheur.setPanel(new Menu());
		}else {
			if(list.getSelectedIndex()!=-1) {
				Launcheur.setPanel(new EditorInstance(list.getSelectedIndex()+1,true));
			}else {
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
