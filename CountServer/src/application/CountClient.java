package application;



import java.io.*;
import java.net.*;
import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.control.ScrollPane;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.Pane;
import javafx.stage.Stage;

public class CountClient extends Application {
  // IO streams
  DataInputStream fromServer = null;

  @Override // Override the start method in the Application class
  public void start(Stage primaryStage) {

	  Pane mainPane = new Pane();
    
	  // Message to display connection
	  Label Message = new Label();
    try {
      // Create a socket to connect to the server
      Socket socket = new Socket("localhost", 8000);
      fromServer = new DataInputStream(socket.getInputStream());
      
      //make the label state the visitation message
      Message.setText("You are visitor: " + String.valueOf(fromServer.readInt()));


    }
    catch (IOException ex) {
      Message.setText(ex.toString() + '\n');
    }

    
    // Create a scene and place it in the stage
    mainPane.getChildren().add(Message);
    Scene scene = new Scene(mainPane, 450, 200);
    primaryStage.setTitle("Client"); // Set the stage title
    primaryStage.setScene(scene); // Place the scene in the stage
    primaryStage.show(); // Display the stage
    
  

  }

  /**
   * The main method is only needed for the IDE with limited
   * JavaFX support. Not needed for running from the command line.
   */
  public static void main(String[] args) {
    launch(args);
  }
}

