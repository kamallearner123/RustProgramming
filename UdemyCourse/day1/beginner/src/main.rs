use std::env;
use std::str::FromStr;

fn main() {
    println!("Hello, world!");
    let mut args: Vec<u32> = Vec::new();
    for arg in env::args().skip(1) {
        args.push(u32::from_str(&arg).
                    expect("error parsing arg!!!"));  
    }

    for arg in args {
        println!("{}",arg);
    }
}
