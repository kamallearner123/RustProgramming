use std::io;

fn main() {
    let mut data = String::new();
    io::stdin().read_line(&mut data).unwrap();
    println!("data = {}", data);

    let num: f32 = data.trim().parse().unwrap();
    println!("nu, = {}", num);
}

