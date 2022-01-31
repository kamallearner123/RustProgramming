fn fibonacci(n: u32) -> u32 {
    match n {
        0 => 1,
        1 => 1,
        _ => let total = fibonacci(n - 1) + fibonacci(n - 2);
            println!("number = {}\n", total);
            total,
    }
}

fn main() {
    println!("{}",fibonacci(10));
}
