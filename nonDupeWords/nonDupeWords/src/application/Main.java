package application;
	

import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;
import java.util.TreeSet;

import javafx.application.Application;
import javafx.stage.FileChooser;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.Pane;
import javafx.scene.text.Text;


public class Main extends Application {
	@Override
	public void start(Stage primaryStage) {
		try {
			Pane root = new Pane();
			
			

			Button fileChoice = new Button("Choose File");
			
			fileChoice.setOnAction(e -> {
				
			FileChooser fileChooser = new FileChooser();
			 fileChooser.setTitle("Open Resource File");
			 File selectedFile = fileChooser.showOpenDialog(primaryStage);
			
			 try {
				Scanner input = new Scanner(selectedFile);
				Set<String> nonDupes = new TreeSet<>();
				
				while(input.hasNext()) {
					
					
					nonDupes.add(input.next());
					
					
				}
				
				Label text = new Label(nonDupes.toString());
				text.setWrapText(true);
				text.setMaxWidth(400);
				text.setLayoutX(50);
				text.setLayoutY(50);
				
				root.getChildren().add(text);
				
			} catch (FileNotFoundException e1) {
				e1.printStackTrace();
			}
			 
			 
			});
			
			 root.getChildren().add(fileChoice);
			 
			
			Scene scene = new Scene(root,500,500);
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
