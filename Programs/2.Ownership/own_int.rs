fn main() {
    let mut  i:i32 = 42;
    let  ref_i: &mut i32 = &mut i;

    ref_i = *ref_i+10;                                                                                                
    println!("ref_i = {}", ref_i);
}
