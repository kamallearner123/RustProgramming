use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("There is no arg!!!");

    let result = input.trim().parse::<f64>();
    println!("result = {:?}", result);

    match result {
        Ok(num) => println!("Number is collected!!! = {}", num),
        Err(msg) => println!("Failed to parse... err = {}", msg)
    }
}
