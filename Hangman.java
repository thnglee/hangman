package org.example;

import java.util.Scanner;

public class Hangman {
    private String wordToGuess;
    private StringBuilder guessedWord;
    private int maxAttempts;
    private int attemptsLeft;
    private StringBuilder usedLetters;

    public Hangman(String wordToGuess, int maxAttempts) {
        this.wordToGuess = wordToGuess.toLowerCase();
        this.maxAttempts = maxAttempts;
        this.attemptsLeft = maxAttempts;
        this.guessedWord = new StringBuilder("_".repeat(wordToGuess.length()));
        this.usedLetters = new StringBuilder();
    }

    public void play() {
        Scanner scanner = new Scanner(System.in);

        while (attemptsLeft > 0) {
            clearConsole();
            System.out.println("Tu can doan: " + guessedWord.toString());
            System.out.println("Co hoi con lai: " + attemptsLeft);
            System.out.println("Cac ki tu da doan: " + usedLetters.toString());
            System.out.print("Nhap 1 ki tu: ");
            String input = scanner.nextLine().toLowerCase();

            if (input.length() == 1 && Character.isLetter(input.charAt(0))) {
                char letter = input.charAt(0);
                if (!usedLetters.toString().contains(String.valueOf(letter))) {
                    usedLetters.append(letter).append(" ");
                    // du ma sai lam vai cut.
                    if (wordToGuess.contains(String.valueOf(letter))) {
                        updateGuessedWord(letter);
                        // neu chua

                    } else {
                        attemptsLeft--;
                        System.out.println("Sai roi em.");
                        drawHangman(maxAttempts - attemptsLeft);
                    }

                    if (guessedWord.toString().equals(wordToGuess)) {
                        System.out.println("Chuc mung! Em doan dung roi do: " + wordToGuess);
                        break;
                    }
                } else {
                    System.out.println("Em doan chu nay roi ma, doan chu khac di!");
                }
            } else {
                System.out.println("Doan 1 chu thoi, dung nhieu hon!");
            }
        }

        if (attemptsLeft == 0) {
            clearConsole();
            drawHangman(maxAttempts);
            System.out.println("Thua rui, tu can doan do la: " + wordToGuess);
        }

        scanner.close();
    }

    private void updateGuessedWord(char letter) {
        for (int i = 0; i < wordToGuess.length(); i++) {
            if (wordToGuess.charAt(i) == letter) {
                guessedWord.setCharAt(i, letter);
            }
        }
    }

    private void drawHangman(int incorrectGuesses) {
        String[] hangmanImages = {
                "  +---+\n  |   |\n      |\n      |\n      |\n      |",
                "  +---+\n  |   |\n  O   |\n      |\n      |\n      |",
                "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |",
                "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |",
                "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |",
                "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |",
                "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |"
        };
        System.out.println(hangmanImages[incorrectGuesses - 1]);
    }

    private void clearConsole() {
        try {
            final String os = System.getProperty("os.name");
            if (os.contains("Windows")) {
                new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
            } else {
                System.out.print("\033[H\033[2J");
                System.out.flush();
            }
        } catch (Exception e) {
            // xu li exception
        }
    }

}
