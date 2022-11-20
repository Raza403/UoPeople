import javax.swing.JOptionPane;

public class SuperPower {
    public static void main(String[] args) {
        // Prompt to user to get input and save the value to variable power.
        String power = JOptionPane.showInputDialog("What is your super power?");
        // Converting the power to uppercase using Java's built in method.
        power = power.toUpperCase();
        JOptionPane.showMessageDialog(null,power+" TO THE RESCUE!");
    }
}
