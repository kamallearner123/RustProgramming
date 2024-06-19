
fn main() {
    let mut a:u8 = 2;

    //Checked
    println!("checked_: {:?}",a.checked_mul(100)); // Some(200)
    println!("checked_: {:?}",a.checked_mul(200)); // None
    

    //unwrap()
    //println!("unwrap: {:?}", a.checked_mul(200).unwrap()); //panic
    println!("unwrap: {:?}", a.checked_mul(50).unwrap()); // no pacnic

    //wrapping()
    println!("wrapping_: {:?}", a.wrapping_mul(250)); // wrapping, no-panic
    println!("wrapping_: {:?}", a.wrapping_mul(100)); // no srapping


    let a:i8 = 10;
    //saturating()
    println!("saturating_: {:?}", a.saturating_mul(30)); // no-wrapping, no-panic, max value
    println!("saturating_: {:?}", a.saturating_mul(-25)); // no-wrapping, no-panic, min value (-ve value)

    
    //overflowing()
    println!("overflowing_: {:?}", a.overflowing_mul(25)); // no-wrapping, no-panic, max value
    println!("overflowing_: {:?}", a.overflowing_mul(-25)); // no-wrapping, no-panic, min value (-ve value)
}


