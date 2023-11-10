package org.example;

import javafx.application.Application;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.control.Button;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.HBox;
import javafx.stage.Stage;
import javafx.scene.text.Text;

public class HangmanGame extends Application {
    // random tu can doan vao day
    private String wordToGuess = "btloop";
    private String currentGuess = "";
    private int maxAttempts = 6;
    private int attemptsLeft = maxAttempts;

    private Text wordDisplay = new Text();
    private Text attemptsDisplay = new Text("Số cơ hội còn lại" + attemptsLeft);
    private Text hangmanDisplay = new Text();

    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) {
        primaryStage.setTitle("Hangman Game");

        wordDisplay.setText(getDisplayWord());
        hangmanDisplay.setText("  O\n /|\\\n / \\");

        HBox wordBox = new HBox(10);
        wordBox.setAlignment(Pos.CENTER);
        wordBox.getChildren().add(wordDisplay);

        GridPane keyboard = createKeyboard();

        HBox attemptsBox = new HBox(10);
        attemptsBox.setAlignment(Pos.CENTER);
        attemptsBox.getChildren().add(attemptsDisplay);

        HBox hangmanBox = new HBox(10);
        hangmanBox.setAlignment(Pos.CENTER);
        hangmanBox.getChildren().add(hangmanDisplay);

        GridPane grid = new GridPane();
        grid.setAlignment(Pos.CENTER);
        grid.add(wordBox, 0, 0);
        grid.add(keyboard, 0, 1);
        grid.add(attemptsBox, 0, 2);
        grid.add(hangmanBox, 0, 3);

        Scene scene = new Scene(grid, 400, 400);
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    private GridPane createKeyboard() {
        GridPane keyboard = new GridPane();
        keyboard.setAlignment(Pos.CENTER);

        char[] alphabet = "abcdefghijklmnopqrstuvwxyz".toCharArray();
        int col = 0;
        int row = 0;

        for (char letter : alphabet) {
            Button button = new Button(String.valueOf(letter));
            button.setOnAction(event -> handleLetterClick(letter));
            keyboard.add(button, col, row);

            col++;
            if (col == 7) {
                col = 0;
                row++;
            }
        }
        return keyboard;
    }

    private void handleLetterClick(char letter) {
        if (attemptsLeft > 0 && !currentGuess.contains(String.valueOf(letter))) {
            if (wordToGuess.contains(String.valueOf(letter))) {
                currentGuess += letter;
            } else {
                attemptsLeft--;
            }
            wordDisplay.setText(getDisplayWord());
            attemptsDisplay.setText("Attempts left: " + attemptsLeft);
            checkGameStatus();
            updateHangmanDisplay();
        }
    }

    private String getDisplayWord() {
        StringBuilder displayWord = new StringBuilder();

        for (char letter : wordToGuess.toCharArray()) {
            if (currentGuess.contains(String.valueOf(letter))) {
                displayWord.append(letter);
            } else {
                displayWord.append("_");
            }
            displayWord.append(" ");
        }
        return displayWord.toString();
    }

    private void checkGameStatus() {
        if (currentGuess.equals(wordToGuess)) {
            displayGameResult("Chúc mừng, đoán đúng rồi đó: " + wordToGuess);
        } else if (attemptsLeft == 0) {
            displayGameResult("Thua rồi, từ cần đoán là: " + wordToGuess);
        }
    }

    private void displayGameResult(String message) {
        Alert alert = new Alert(AlertType.INFORMATION);
        alert.setTitle("Game Result");
        alert.setHeaderText(null);
        alert.setContentText(message);
        alert.showAndWait();
    }

    private void updateHangmanDisplay() {
        int incorrectGuesses = 0;
        for (char letter : currentGuess.toCharArray()) {
            if (!wordToGuess.contains(String.valueOf(letter))) {
                incorrectGuesses++;
            }
        }

        switch (incorrectGuesses) {
            case 1:
                hangmanDisplay.setText("  O\n /|\\\n /");
                break;
            case 2:
                hangmanDisplay.setText("  O\n /|\\\n  ");
                break;
            case 3:
                hangmanDisplay.setText("  O\n /|  \n  ");
                break;
            case 4:
                hangmanDisplay.setText("  O\n /|  \n    ");
                break;
            case 5:
                hangmanDisplay.setText("  O\n /|  \n    ");
                break;
            case 6:
                hangmanDisplay.setText("  X\n /|\\ \n / \\");
                break;
        }
    }
}
