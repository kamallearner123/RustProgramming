use std::io;
fn main() {
    let mut a = String::new();
    let result = io::stdin().read_line(&mut a);
    process(&a);
    println!("{:?}", result);
    println!("{}", a);
}

fn process(a: &String) {
    println!("{}", a);
}
