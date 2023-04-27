use rand::Rng;

fn main() {
    let mut rng = rand::thread_rng();
    let random_numbers: Vec<u32> = (0..50).map(|_| rng.gen_range(1..=100)).collect();
    
    let mut list_of_numbers = String::new();
    for num in random_numbers {
        list_of_numbers.push_str(&num.to_string());
    }
    println!("{}", list_of_numbers);
}
