public class example7 {
  public static void main(String[] args){
    // Calculate factorial of 5.
    // Initialize int fact and number.
    int fact = 1;
    int number = 5;
    // Run a for loop until i reaches number.
    for (int i = 1; i <= number; ++i) {
      // Calculate the factorial.
        fact *= i;
    }
    // Print the factorial.
    System.out.println(fact);
  }
}
