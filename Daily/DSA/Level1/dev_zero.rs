fn main() {
    let a:i32 = 10;
    let b:i32 = 2;
    match a.checked_div(b) {
        Some(v) => println!("Val = {}", v),
        None => println!("None")
    }
}