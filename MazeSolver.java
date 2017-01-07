import java.awt.*;
import java.awt.event.*;
import javax.swing.*;        

/**
 *  Class that runs a maze display/solution GUI
 *
 *  @author Nicholas R. Howe
 *  @version CSC 112, 20 March 2006
 */
public class MazeSolver extends JApplet {
    /** Holds the maze to solve */
    private static Maze maze;

    /** The window */
    private static JFrame frame;

    /** Solve button */
    private static JButton solveButton;

    /** Reset button */
    private static JButton resetButton;

    public static void createAndShowGUI() {
        // Make sure we have nice window decorations.
        JFrame.setDefaultLookAndFeelDecorated(true);

        // Create and set up the window.
        frame = new JFrame("Maze Application");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

	// Add components
	createComponents(frame.getContentPane());

        // Display the window.
        frame.pack();
        frame.setVisible(true);
    }

    public static void createComponents(Container pane) {
	pane.add(maze);
	JPanel panel = new JPanel();
	panel.setLayout(new FlowLayout());
	solveButton = new JButton("Solve");
	solveButton.addActionListener(new SolveListener());
	panel.add(solveButton);
	resetButton = new JButton("Reset");
	resetButton.addActionListener(new ResetListener());
	panel.add(resetButton);
	pane.add(panel,BorderLayout.SOUTH);
    }

    // Application starts here
    public static void main(String[] args) {
        if (args.length == 0) {
            maze = new Maze();
        } else {
            maze = new Maze(args[0]);
        }
        // Schedule a job for the event-dispatching thread:
        // creating and showing this application's GUI.
        javax.swing.SwingUtilities.invokeLater(new Runnable() {
		public void run() {
		    createAndShowGUI();
		}
	    });
    }

    // Applet starts here
    public void init() {
	//Execute a job on the event-dispatching thread:
	//creating this applet's GUI.
	try {
	    javax.swing.SwingUtilities.invokeAndWait(new Runnable() {
		    public void run() {
			createComponents(getContentPane());
		    }
		});
	} catch (Exception e) {
	    System.err.println("createGUI didn't successfully complete");
	}
    }

    /** Event handler for Solve button */
    private static class SolveListener implements ActionListener {
	public void actionPerformed(ActionEvent e) {
	    maze.reset();
	    // call to solve should be on a new thread
	    solveButton.setEnabled(false);
	    resetButton.setEnabled(false);
	    (new SolverThread()).execute();
	}
    }

    /** Event handler for Reset button */
    private static class ResetListener implements ActionListener {
	public void actionPerformed(ActionEvent e) {
	    maze.reset();
	}
    }

    /** Worker class for solving the maze */
    private static class SolverThread extends SwingWorker<Boolean, Object> {
       @Override
       public Boolean doInBackground() {
           return maze.solve();
       }

       @Override
       protected void done() {
           try {
	       if (!get()) {  // test the result of doInBackground()
		   System.out.println("Maze has no valid solution.");
	       }
	       solveButton.setEnabled(true);
	       resetButton.setEnabled(true);
           } catch (Exception ignore) {
           }
       }
   }
}
