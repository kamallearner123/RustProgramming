use std::io;

fn main() {
    let mut a = String::new();
    let result;
    result = io::stdin().read_line(&mut a);
    println!("{},{:#?}", a, result);
}
