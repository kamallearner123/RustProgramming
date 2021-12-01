fn printall(sub_array: &mut [u32]) {
    let i:u32 = 0;

    for i:u32 in 0..sub_array.len() {
        sub_array[i] = i*2;
        println!(" i = {}, val = {}", i, sub_array[i]);

    }
}

use std::mem;
fn main() {
    let mut x:[u32; 100] = [1;100];

    println!("x[3] = {}", x[3]);
    println!(" size of array = {}", mem::size_of_val(&x));

    printall(&mut x[0..90]);

    let i:u32;

    for i in 0..x.len() {
        println!("x[{}] = {}", i,x[i]);
    }
}
