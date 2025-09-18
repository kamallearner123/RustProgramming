use std::io;

fn main() {
    let mut input:String = String::new();
    io::stdin().read_line(&mut input).expect("Not able to read the data from comand line");
    println!("Read line is {}", input);
}
