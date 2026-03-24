fn main() {
    let mut ptr = Box::new(100_i32);
    *ptr = 10;
    println!("ptr = {}", ptr);
}
