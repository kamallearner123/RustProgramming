

fn main() {
    let a: [u32; 3] = [1,2,3];
    println!("len = {}", a.len());
    for i in 0..a.len() {
        println!("{}",a[i]);
    }

    let mut b: [u32; 3] = [3,4,5];
    for i in 0..a.len() {
        b[i] = a[i];
    }
}