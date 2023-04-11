import java.util.Random;

public class Randoms {
    public int getRandom(){
        Random rand = new Random();
        return rand.next();
    }

    public static void main(String[] args){
        System.out.println(getRandom());
    }
}