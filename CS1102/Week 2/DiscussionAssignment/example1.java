public class example1 {
  public static void main (String[] args) {
    System.out.println("Here are all the even numbers from 0 to 10");
    // Initiate integer i
    int i = 1;
    // Start the while loop, will terminate when i >=5.
    while (i <= 5) {
      // Multiply by 2 to get the even numbers.
      System.out.println(2*i);
      // Increment the i, otherwise this will be an infinite loop.
      i++;
    }
  }
}