fn main() {
    let x:u32 = 10;
    let y:u32 = 10;

    for (x,y) in (100..1000).enumerate() {
        println!("x = {}, y = {}\n", x,y);
    }
}

