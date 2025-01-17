#include <Wire.h>
#include <Arduino.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C Icd(0x27, 26, 2);
const int ledPin0 = A0;   // red
const int ledPin1 = A1;   // green
const int buttonP1 = A2;  // p1
const int buttonP2 = A3;  // p2

bool gameActive = false;
bool countdownStarted = false;
unsigned long countdownStartTime;
const unsigned long countdownDuration = 10000;  // 10 seconds

int buttonCountP1 = 0;
int buttonCountP2 = 0;

void setup() {
  Icd.init();
  Icd.backlight();
  pinMode(ledPin0, OUTPUT);
  pinMode(ledPin1, OUTPUT);
  pinMode(buttonP1, INPUT);
  pinMode(buttonP2, INPUT);
}

void loop() {
  // Start
  if (!gameActive) {
    Icd.setCursor(2, 0);
    Icd.print("P1: " + String(buttonCountP1));
    Icd.setCursor(9, 0);
    Icd.print("P2: " + String(buttonCountP2));
    Icd.setCursor(0, 1);
    Icd.print("Press two button");


    if (digitalRead(buttonP1) == HIGH && digitalRead(buttonP2) == HIGH) {
      gameActive = true;
      countdownStarted = false;
      digitalWrite(ledPin1, HIGH);
      Icd.clear();
      Icd.setCursor(3, 0);
      Icd.print("1");
      delay(700);
      Icd.setCursor(6, 0);
      Icd.print(" 2 ");
      delay(700);
      Icd.setCursor(11, 0);
      Icd.print("3");
      delay(600);
      Icd.setCursor(5, 1);
      Icd.print("Go!!!!");
      delay(600);
      Icd.clear();
      Icd.setCursor(3, 0);
      Icd.print("--Press!--");
      Icd.setCursor(1, 1);
      Icd.print("-The Buttons!-");
      buttonCountP1 = 0;  // Reset button counts
      buttonCountP2 = 0;
    } else {
      if (digitalRead(buttonP1) == LOW && digitalRead(buttonP2) == LOW) {
        gameActive = false;
        digitalWrite(ledPin0, HIGH);
        delay(500);
        digitalWrite(ledPin0, LOW);
      }
    }
  } else {
    // Game is active
    if (!countdownStarted) {
      countdownStarted = true;//star time
      countdownStartTime = millis();// Countdown amount of time
    }

    if (millis() - countdownStartTime >= countdownDuration) {
      gameActive = false;//stop game
      countdownStarted = false;//stop time
      digitalWrite(ledPin1, LOW);
      digitalWrite(ledPin0, HIGH);
      delay(500);
      digitalWrite(ledPin0, LOW);
      // Display button counts and winner
      Icd.clear();
      Icd.setCursor(2, 0);
      Icd.print("P1: " + String(buttonCountP1));
      Icd.setCursor(6, 1);
      Icd.print("P2: " + String(buttonCountP2));

      if (buttonCountP1 > buttonCountP2) {
        Icd.setCursor(5, 1);
        Icd.print("P1 Wins!");
      } else if (buttonCountP2 > buttonCountP1) {
        Icd.setCursor(5, 1);
        Icd.print("P2 Wins!");
      } else {
        Icd.setCursor(4, 1);
        Icd.print("It's a Tie!");
      }
      delay(5000);  // Display result for 5 seconds
      Icd.clear();
    }

    // Check button presses and count
    if (digitalRead(buttonP1) == HIGH) {
      buttonCountP1++;
      delay(200);  // Debounce delay
    }
    if (digitalRead(buttonP2) == HIGH) {
      buttonCountP2++;
      delay(200);  // Debounce delay
    }
  }
}
