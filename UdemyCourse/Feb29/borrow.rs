use std::io;

fn main() {
    let mut A = String::new();
    io::stdin().read_line(&mut A);
    let mut a = &mut A;
    let b = &A;


    println!("A = {}, a = {}, b={}", A, a, b);
    println!("A = {}", A);
}
