using System;
using System.IO;

namespace RandomTest {
    class Randoms {
        public static int getRandom(){
            var rand = new Random();
            return rand.Next();
        }

        static void Main(String[] args){
            for(int i = 0; i < 50; i++) {
                File.AppendAllText("c_sharp_random.txt", getRandom().ToString());
            }
        }
    }
}