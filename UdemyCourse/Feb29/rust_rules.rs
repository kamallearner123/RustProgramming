use std::io;

fn main() {
    println!("Hello... let us practice rules");
    let mut a = Default::default();
    let result;
    result = io::stdin().read_line(&mut a);
    let b = a;
    println!("a={}, result ={:#?}", b, result);
}

