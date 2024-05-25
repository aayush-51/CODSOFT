import java.util.Scanner;
import java.lang.Math;

public class Number_Game {
  public static void guessing_game() {
    
    int number = (int)(Math.random() * 100) + 1;
    int k = 5; int i;
    int noOfGuesses = 0;
    
    Scanner input = new Scanner(System.in);
    
    System.out.println("I'm thinking of a number between 1 and 100.\nYou have 5 tries to guess the number.\n");
    
    for (i = 0; i < k; i++) {
     System.out.print("Enter your guess: ");
     int guess = input.nextInt();
     noOfGuesses++;
      
      if (guess == number) {
        System.out.println("You guessed the number!\nYou win!\nYou guessed it in " + noOfGuesses + " attempts! ");
        break;
      }
      
      else if (guess > number) {
        System.out.println("Your guess is too high.\nYou have " + (k - i - 1) + " tries left.\n");
      }
      
      else {
        System.out.println("Your guess is too low.\nYou have " + (k - i - 1) + " tries left.\n");
      }
    }
    
    if (i == k) {
      System.out.println("You ran out of tries.\nYou lose!");
    }
    System.out.println(	"The number was " + number);
    
    System.out.println("\n do you want to give another try? \n if yes then press 1 else 0 ");
    int choice = input.nextInt();
    
    if (choice == 1){
        guessing_game();
    }else 
    return;
  }

public static void main(String args[]) {
    guessing_game();
}
}

