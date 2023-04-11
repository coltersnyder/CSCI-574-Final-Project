use rand::Rng;

fn main(){
    let mut rng = rand::thread_rng();

    let n: u16 = rng.gen()
    println!("Random u16: {}", n);
}