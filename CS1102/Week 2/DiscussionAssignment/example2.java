public class example2 {
  public static void main(String[] args) {
    System.out.println("Here are all the even numbers from 0 to 10");
    // Initiate integer i
    int i = 1;
    // Run the while loop
    do {
      // Multiply by 2 to get the even numbers.
      System.out.println(2 * i);
      // Increment the i, otherwise this will be an infinite loop.
      i++;
    }
    // Check the condition and run the loop again only
    // if the value of i is less than or equal to 5.
    while (i <= 5);
  }
}
