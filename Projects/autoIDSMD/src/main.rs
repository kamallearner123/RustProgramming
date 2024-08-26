
use std::env;

fn sample(data:i32) -> Result<i32,String> {
    if data>100 {
        Ok(0)
    } else {
        Err("less value".to_string())
    }
}

fn main() {
    let args: Vec<String> = env::args().collect();
    println!("Len of env = {}", args.len());

    println!("Hello, world!");
    let a = match sample(400) {
        Ok(result) => println!("Value = {}", result),
        Err(errno) => println!("Error: {}", errno)
    };

    println!("a = {:?}", a);
}
