macro_rules! log {
    ($($arg:tt)*) => {
        println!($($arg)*);
    };
}

fn main() {
    let name = String::from("Kamal");
    let num = 10;

    log!("Name {}, RollNo {}", name, num);
}

