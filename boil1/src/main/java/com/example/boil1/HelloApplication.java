package com.example.boil1;

import javafx.application.Application;
import javafx.beans.property.SimpleStringProperty;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.Insets;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.TextField;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.scene.text.Text;
import javafx.stage.Stage;

import java.io.IOException;
import java.util.*;

public class HelloApplication extends Application {

    private TableView table = new TableView();
    Map<String, Task> allTasks = new HashMap<String, Task>();
    HashSet<Task> tasks = new HashSet<Task>();
    Task End = new Task("End", 0);
    Task J = new Task("J", 2, End);
    Task I = new Task("I", 1, J);
    Task E = new Task("E", 1, I);
    Task D = new Task("D", 7, E);
    Task B = new Task("B", 4, D);
    Task F = new Task("F", 2, I);
    Task H = new Task("H", 4, I);
    Task G = new Task("G", 3, H);
    Task C = new Task("C", 6, G,F);
    Task A = new Task("A", 3, B, C);
    Task Start = new Task("Start", 0, A);
    private final ObservableList<Task> data =
            FXCollections.observableArrayList(
                    End, J, I, E, D, B, F, H, G, C, A, Start
            );
   final HBox hb = new HBox();

    @Override
    public void start(Stage stage) throws IOException {
        tasks.add(End);
        tasks.add(J);
        tasks.add(I);
        tasks.add(H);
        tasks.add(G);
        tasks.add(F);
        tasks.add(E);
        tasks.add(D);
        tasks.add(C);
        tasks.add(B);
        tasks.add(A);
        tasks.add(Start);
        Scene scene = new Scene(new Group());
        stage.setTitle("CPM");
        stage.setWidth(500);
        stage.setHeight(650);


        // Create columns
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

                String name_n = addName.getText();
                int cost_n = Integer.parseInt(addCost.getText());
                String dep_n = addDependencies.getText();
                allTasks.put(name_n, new Task(name_n, cost_n));
                String[] arrOfStr = dep_n.split(",");
                for (String s : arrOfStr) {
                    allTasks.get(name_n).addDependency(allTasks.get(s));
                }
                allTasks.get(name_n).setDep_names();
                data.add(allTasks.get(name_n));
                tasks.add(allTasks.get(name_n));
                addName.clear();
                addCost.clear();
                addDependencies.clear();
            }
        });

        final Button clearButton = new Button("Clear");
        clearButton.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent actionEvent) {
                allTasks.clear();
                tasks.clear();
                table.getItems().clear();
            }
        });

        final Button calculateButton = new Button("Calculate");
        calculateButton.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent actionEvent) {
                Stage stage_n = new Stage();
                stage_n.setTitle("Summary");

                Task[] result = CriticalPath.criticalPath(tasks);
//                String summary = CriticalPath.print(result);

                Text text = new Text();
//                text.setText(summary);
                text.setX(20);
                text.setY(20);

                Collection<String> list = new ArrayList<>();
                list = CriticalPath.print(result);

                ObservableList<String> details = FXCollections.observableArrayList(list);

                TableView<String> tableViewS = new TableView<>();
                TableColumn<String, String> col1 = new TableColumn<>();
                tableViewS.getColumns().addAll(col1);
                tableViewS.prefHeightProperty().bind(stage_n.heightProperty());
                tableViewS.prefWidthProperty().bind(stage_n.widthProperty());

                col1.setCellValueFactory(data -> new SimpleStringProperty(data.getValue()));
                tableViewS.setItems(details);

                Group root = new Group(tableViewS);
                Scene scene_n = new Scene(root, 400, 500);
                stage_n.setScene(scene_n);
                stage_n.show();
            }
        });

        hb.getChildren().addAll(addButton);
        hb.setSpacing(3);

        final VBox vbox = new VBox();

        vbox.setSpacing(5);
        vbox.setPadding(new Insets(10,0,0,10));
        vbox.getChildren().addAll(table, addName, addCost, addDependencies, addButton, calculateButton, clearButton);


        ((Group) scene.getRoot()).getChildren().addAll(vbox);


        stage.setScene(scene);
        stage.show();

    }

    public static void main(String[] args) {
        launch();
    }
}


