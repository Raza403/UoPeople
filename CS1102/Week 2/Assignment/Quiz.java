// Import JOptionPane to use dialoge box.
import javax.swing.JOptionPane; 
public class Quiz {
  public static void main(String[] args) {
    String question = "This assignment is for?\n";
    // Adding all the options to the questions.
    question += "A. Week 1\n";
    question += "B. Week 2\n";
    question += "C. Week 3\n";
    question += "D. Week 4\n";         
    question += "E. None of the above options.";
    while (true) {
      // Take answer from the user.
      String answer = JOptionPane.showInputDialog(question);
      // Uppercase the answer, so that we can match. 
      answer = answer.toUpperCase();
      // Check if answer is correct.
      if (answer.equals("B")) {
        // Show message in case of correct answer.
        JOptionPane.showMessageDialog(null,"Correct!");
        // Break the while loop.
        break;
      }
      // Check if the answer is from any incorrect answers.
      else if(answer.equals("A") || answer.equals("C") || answer.equals("D") || answer.equals("E")){
        // Show message incorrect option selected.
        JOptionPane.showMessageDialog(null,"Incorrect. Please try again."); 
      }
      // Otherwise answer is invalid.
      else{
        // Show message for invalid answer.
        JOptionPane.showMessageDialog(null,"Invalid answer. Please enter A, B, C, D, or E.");
      }
    }
  }
}