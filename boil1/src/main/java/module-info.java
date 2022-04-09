module com.example.boil1 {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.boil1 to javafx.fxml;
    exports com.example.boil1;
}