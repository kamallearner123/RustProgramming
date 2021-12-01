
fn change(val mut:&u32) {
    val =200;
}

fn main() {

    let mut a: u32;
    a = 100;
    change(&a);
    println!("a = {}",a);
}
