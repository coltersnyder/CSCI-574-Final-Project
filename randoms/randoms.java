import java.util.Random;

public class Randoms {

    public static void main(String[] args){
        Random rand = new Random();
        int[] listOfRandomNumbers = new int[50];
        for (int i = 0; i < 50; i++) {
            listOfRandomNumbers[i] = rand.nextInt(100) + 1;
        }
        
        // This printed string is "String Data File" for the Test Suite input.
        String listOfNumbers = "";
        for(int index : listOfRandomNumbers) {
            listOfNumbers += index;
        }
        System.out.println(listOfNumbers);
    }
}
