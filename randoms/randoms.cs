using System;
using System.Random;
using System.IO;

namespace RandomTest {
    class Randoms {
        public int getRandom(){
            var rand = new Random();
            return rand.NextInt();
        }

        static void Main(String[] args){
            for(int i = 0; i < 50; i++) {
                File.AppendAllText("c_sharp_random.txt", getRandom.ToString());
            }
        }
    }
}