using System;
using System.Random;

namespace RandomTest {
    class Randoms {
        public int getRandom(){
            var rand = new Random();
            return rand.NextInt();
        }

        static void Main(String[] args){
            Console.WriteLine(getRandom());
        }
    }
}