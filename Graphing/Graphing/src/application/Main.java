package application;

//IUmporting all thats needed for the project
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;
import graphUtil.*;
import graphUtil.UnweightedGraph.SearchTree;
import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.Pane;


public class Main extends Application {
	
	//Creating the needed variables for the project
	ArrayList<Integer> Vertices = new ArrayList<>();
	ArrayList<Edge> Edges = new ArrayList<>();
	int numOfVert;
	Boolean Connected;
	@Override
	public void start(Stage primaryStage) {
		
		//Try catch for the jfx program
		try {
			//creating of the visual components 
			Pane root = new Pane();
			Label graphfilerequest = new Label("Please give file name of the graph: ");
			TextField graphfilename = new TextField();
			Button Submit = new Button("Submit");
			Label graphInfo = new Label();
			Submit.setOnAction(new EventHandler<ActionEvent>() {
				
				
				//Handle for the button set action to make it open the given file
		        @Override
		        public void handle(ActionEvent event) {
		            File graphFile = new File(graphfilename.getText());
		            
		            try {
		            	//open a reader for the file
						Scanner fileData = new Scanner(graphFile);
						
						
						//get the num of verts from the top line on the file
						numOfVert = fileData.nextInt();
						
						//for how many verts there are
						for(int i = 0; i < numOfVert; i++) {
							
							//take the next line and turn it into a string
							String unCutEdges = fileData.nextLine();
							//Add said string into an array of unpolished edges
							String[] unBuiltEdges = unCutEdges.split(",");
							//add the verts to the list of verts to keep track
							Vertices.add(Integer.parseInt(unBuiltEdges[0]));
							
							//use the lengh of the unpolished edges array
							for (int j = 1; j < unBuiltEdges.length; j++) {
								
								//Add the cleaned up edges to the edge list
								Edge temp = new Edge(Integer.parseInt(unBuiltEdges[0]), Integer.parseInt(unBuiltEdges[j]));
								Edges.add(temp);
								
							}
							
						}
						//using the verts and edges from before make a full graph
						UnweightedGraph<Integer> Graph = new UnweightedGraph<Integer>(Edges, numOfVert);
						String Edges = Graph.printEdges();
						
						//make a tree from the graph so we can check it's connected
						SearchTree Tree = Graph.dfs(numOfVert);
						
						//The if to check connectivity 
						if (numOfVert == Tree.getNumberOfVerticesFound()) {
						
						//If connected
						Connected = true;
						
						} else {
							
							//If not
							Connected = false;
							
						}
						
						//Combine the relevant data into one pile
						String info = graphfilename.getText() + String.valueOf(numOfVert) + Edges + Connected.booleanValue();
						
						//Show compiled data
						graphInfo.setText(info);
						
					} catch (FileNotFoundException e) {
						
						e.printStackTrace();
					}
		        }
		    });
			
			//Activating the visual components 
			graphfilerequest.setTranslateX(0);
			graphfilerequest.setTranslateY(0);
			graphfilename.setTranslateX(30);
			graphfilename.setTranslateY(30);
			Submit.setTranslateX(40);
			Submit.setTranslateY(70);
			graphInfo.setTranslateX(300);
			graphInfo.setTranslateY(600);
			root.getChildren().add(graphfilerequest);
			root.getChildren().add(graphfilename);
			root.getChildren().add(Submit);
			root.getChildren().add(graphInfo);
			Scene scene = new Scene(root,1000,1000);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public static void main(String[] args) {
		launch(args);
	}
}
