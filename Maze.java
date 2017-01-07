import java.io.*; 
import java.util.*;
import javax.swing.*; 
import java.awt.*; 


/**
 *  This class stores information about the maze and ways to change its display. 
 *
 *  @author Ji Won Chung 
 *  @version November 4, 2016 
 */
public class Maze extends JComponent{
   
    /** This keeps track of the original maze information that we read in from the user */
    private ArrayList<String> mazeStorage = new ArrayList <String>();
   
    /** This keeps track of the height of the mazeGrid. */
    private int height; 

    /** This keeps track of the width of the mazeGrid. */
    private int width; 

    /** This keeps track of the info of the maze. */
    private MazeContents[][] mazeGrid; 

    /** This keeps track of the magnification. */
    public static int magnify = 30;

    /** Point that keeps track of the coordinates of the starting position in the maze */
    private MazeCoordinate startPoint; 
    
    /** Point htat keeps track of the coordinates of the ending position in the maze */
    private MazeCoordinate endPoint; 

    /** Constructor of a maze object when input is via input redirection. */
    public Maze(){ 
	BufferedReader mazeRawData = new BufferedReader(new InputStreamReader(System.in)); //read in the maze data from input
	createMaze(mazeRawData); //creates the maze and the graphical display 
    }

    /**
     *  Constructor of a maze object when input is via command line. 
     * 
     *  @param fname The name of the file that includes information regarding the maze. 
     */
    public Maze(String fname){
	try {
	    BufferedReader mazeRawData = new BufferedReader(new FileReader(fname)); //read in the maze data from file 
	    createMaze(mazeRawData); //creates the maze and the graphical display
	} catch (IOException e) {
	    System.err.println("Problem reading file "+fname);
	    System.exit(-1);
	}
    }
    
    /** Accessor that returns the height of the maze. */
    public int getMazeHeight(){ 
	return this.height;
    } 

    /** Accessor that returns the width of the maze. */
    public int getMazeWidth(){ 
	return this.width; 
    }
    
    /** Accessor that returns the starting point of the maze. */
    public MazeCoordinate getStartPoint(){ 
	return this.startPoint; 
    }

    /** Accessor that returns the ending point of the maze. */
    public MazeCoordinate getEndPoint(){ 
	return this.endPoint; 
    } 

    /** 
     *  Sets the scale of the maze. 
     * 
     *  @param scale The amount the user wants to scale the maze to. 
     */
    public static void setScale(int magnification){ 
	magnify = magnification; 
    }

    /** 
     *  Manipulator that sets the specific values on the maze, based on indices.
     *
     *  @param row The index of the row. 
     *  @param col The index of the column. 
     *  @status status The type of content you want to set that element in the maze to. 
     */
    public void setValue(int row, int col, MazeContents status){ 
	this.mazeGrid[row][col] = status; 
    }
    

    /**
     *  Manipulator that resets the maze to its orignal state. 
     */
    public void reset(){
	setMazeGrid(mazeStorage); //reset the mazeGrid to the original maze given  
	repaint(); 
	try {
	    Thread.sleep(25);
	} catch (InterruptedException ignore) {
	}
    }

    /** 
     *  Manipulator that solves the maze. 
     */
    public boolean solve(){
	MazeCoordinate currentLocation = new MazeCoordinate(startPoint);
	return recursion(currentLocation); 
    }
   
    /** 
     *  The recursion method that will solve the maze. 
     * 
     *  @param currentLocation The location at which you want to start the recursion 
     */
    public boolean recursion(MazeCoordinate currentLocation){ 
	//info on the current location on the maze 
	int col = currentLocation.getCol(); 
	int row = currentLocation.getRow();
	
	//dimensions of this maze 
	int width = this.getMazeWidth(); 
	int height = this.getMazeHeight();
 
	boolean result = false; //default 
	
	if(currentLocation.equals(endPoint)){ //if you've reached the final destination 
	    setValue(row, col, MazeContents.VISITED); //set the final square as visited
	    setValue(row,col, MazeContents.PATH); //set the final square as a path 
	    return true; //indicate that you've found it 
	}else if ((col >= width) || (row >= height) || (col < 0) || (row < 0)){ //if you're out of bounds 
	    return false; //indicate that you haven't found the maze 
	} 
	else if(col < width && row < height){ //if within the boundaries of the maze
	    if(mazeGrid[row][col].isTraversible()){ //if there is a path that you can go to 
		setValue(row, col, MazeContents.VISITED); //indicate that it is visited
		result = recursion(currentLocation.neighbor(MazeDirection.NORTH)) || recursion(currentLocation.neighbor(MazeDirection.SOUTH))|| recursion(currentLocation.neighbor(MazeDirection.EAST))|| recursion(currentLocation.neighbor(MazeDirection.WEST)); //if any of these are true 
		
		if(result){ 
		    setValue(row,col, MazeContents.PATH); 
		} else{ 
		    setValue(row,col, MazeContents.DEAD_END); 
		}
	    } 
	} 

	repaint(); 
	try {
	    Thread.sleep(25); 
	} catch (InterruptedException ignore) {
	}
	return result; 
    }
    
    /** 
     *  Takes in the information of the maze and creates a 2d MazeContents array and the display window.   
     *
     *  @param mazeData the raw information that will be used to create the maze. 
     */
    public void createMaze(BufferedReader mazeData){
	readMaze(mazeData); //reade the data of the maze
	setMazeDimensions(); //set the dimensions of the maze
	setMazeGrid(this.mazeStorage); //crete the 2d MazeContents array of the maze

	//set the dimensions of the display 
	setMinimumSize(new Dimension(width*magnify, height*magnify));   
	setPreferredSize(new Dimension(width*magnify, height*magnify)); 
    } 
    
    /** 
     *  Read the maze data and store it in side an arraylist. 
     * 
     *  @param mazeData The raw information that will be used to be stored in mazeStorage. 
     */
    public void readMaze(BufferedReader mazeData){
	Scanner sc = new Scanner(mazeData); 
	while(sc.hasNextLine()){ //as long as there is a next line for the maze
	    this.mazeStorage.add(sc.nextLine());//add the nextline to mazeStorage
	} 
    }  


    /** 
     *  Sets the dimensions of the maze. 
     */
    protected void setMazeDimensions(){
	if(!mazeStorage.isEmpty()){ //as long as the maze is not empty
	    this.height = mazeStorage.size(); //set the height of the maze
	    this.width = mazeStorage.get(0).length(); //set the width of the maze 
	}
    }
	

    /** 
     *  Manipulator that creates a MazeContents 2d array given the information of the maze. 
     * 
     *  @param mazeInfo the information of the maze that will be needed to create mazeGrid. 
     */
    public void setMazeGrid(ArrayList<String> mazeInfo){
	//set up the mazeGrid 
	int height = this.getMazeHeight(); 
	int width = this.getMazeWidth();
	this.mazeGrid = new MazeContents[height][width];
	
	//loop through the mazeInfo to set the mazeGrid 
	for(int row = 0; row < height; row++){ 
	    char[] lineArray; 
	    lineArray = mazeInfo.get(row).toCharArray(); 
	    for( int column = 0; column < width; column++) { 
		if(lineArray[column] == '#') { 
		    setValue(row, column, MazeContents.WALL); 
		}if (lineArray[column] == '.'){ 
		    setValue(row, column, MazeContents.OPEN); 
		}if(lineArray[column] == 'S'){ 
		    setValue(row, column, MazeContents.OPEN); 
		    startPoint = new MazeCoordinate(row, column); //store the starting point 
		} if(lineArray[column] == 'F') { 
		    setValue(row, column, MazeContents.OPEN);
		    endPoint = new MazeCoordinate(row,column);//store the ending point  
		}
	    }
	}
	
    }

   

    /**
     *  Draws the series of colored squares from a mazeGrid in the graphics window.
     *
     *  @param g The graphics object to draw into.
     */
    public void paintComponent(Graphics g) {
	Color c; 

	//Color parts of the window outside of the maze as black 
	g.setColor(Color.BLACK);
	g.fillRect(0, 0, width*magnify, height*magnify);
	
	//information regarding the starting and endingpoints of the maze 
	int endPointX = endPoint.getCol(); 
	int endPointY = endPoint.getRow()+1;
	int startPointX = startPoint.getCol(); 
	int startPointY = startPoint.getRow()+1; 
	
	//for loop through to paint on the maze with the information given in the maze
	for (int m = 0; m < height; m++){
	    for (int n = 0; n < width; n++){

		//retrieve the color in the maze based on indices
		c = mazeGrid[m][n].getColor();
		
		//set the color of the graphics object
		g.setColor(c);
		
		//fill in pixel in respect to the magnification scale
		g.fillRect(n*magnify, m*magnify, magnify, magnify);

		//indicates the starting and ending points of the maze
		g.setColor(Color.PINK); 
		g.drawString("S", startPointX*magnify, startPointY*magnify); 
		g.drawString("F", endPointX*magnify, endPointY*magnify);

	    }
	}
    }

}


