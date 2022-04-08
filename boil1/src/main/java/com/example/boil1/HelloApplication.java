package com.example.boil1;

import javafx.application.Application;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.geometry.Insets;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.TextField;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.layout.AnchorPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;

public class HelloApplication extends Application {

    private TableView table = new TableView();
    private final ObservableList<Task> data =
            FXCollections.observableArrayList(
                    new Task("A", 5),
                    new Task("B", 4),
                    new Task("End", 0)
            );
   final HBox hb = new HBox();


    @Override
    public void start(Stage stage) throws IOException {

        Scene scene = new Scene(new Group());
        stage.setTitle("CPM");
        stage.setWidth(800);
        stage.setHeight(800);




        TableColumn name = new TableColumn("Nazwa czynności:");
        name.setMinWidth(150);
        name.setCellValueFactory(new PropertyValueFactory<Task, String>("name"));

        TableColumn cost = new TableColumn("Koszt:");
        cost.setMinWidth(100);
        cost.setCellValueFactory(new PropertyValueFactory<Task, Integer>("cost"));

        TableColumn dep_names = new TableColumn("Następnik:");
        dep_names.setMinWidth(100);
        dep_names.setCellValueFactory(new PropertyValueFactory<Task, ArrayList<String>>("dep_names"));


        table.setItems(data);
        table.getColumns().addAll(name, cost, dep_names);


        final TextField addName = new TextField();
        addName.setPromptText("Nazwa");
        addName.setMaxWidth(name.getPrefWidth());
        final TextField addCost = new TextField();
        addCost.setMaxWidth(cost.getPrefWidth());
        addCost.setPromptText("Koszt");
        final TextField addDependencies = new TextField();
        addDependencies.setMaxWidth(dep_names.getPrefWidth());
        addDependencies.setPromptText("Następnik");



        final Button addButton = new Button("Add");
        addButton.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent e) {

                String n = addName.getText();
                int c = Integer.parseInt(addCost.getText());
                ArrayList<String> d = new ArrayList<String>(Arrays.asList(addDependencies.getText()));

                Task t = new Task(n, c);
                t.setDep_names(d);
                data.add(t);
                addName.clear();
                addCost.clear();
                addDependencies.clear();


            }
        });


        hb.getChildren().addAll(/* add...*/ addButton);
        hb.setSpacing(3);

        final VBox vbox = new VBox();

        vbox.setSpacing(5);
        vbox.setPadding(new Insets(10,0,0,10));
        vbox.getChildren().addAll(table);


        ((Group) scene.getRoot()).getChildren().addAll(vbox);

        stage.setScene(scene);
        stage.show();

    }

    public static void main(String[] args) {
        launch();
    }
}


