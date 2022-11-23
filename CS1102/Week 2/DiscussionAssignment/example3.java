public class example3 {
  public static void main(String[] args) {
    System.out.println("Here are all the even numbers from 0 to 10");
    // In the step below we are doing 3 things.
    // Initializing int i with an initial value of 1.
    // Checking if i<=5, this step is done is all the iterartions.
    // Increment the i by one. 
    for(int i=1; i<=10; i++){
      // if remainder fo i/2==0?
      // if yes, i is even, else odd.
      if(i%2 == 0){
        // Print the even value of
        System.out.println(i);
      }
    }
  }
}
