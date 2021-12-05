
//Find GCD
fn gcd(mut m:u32, mut n:u32) -> u32 {
    assert!(m!=0 && n!=0);
    while m != 0{
        if m<n {
            let i = n;
            n = m;
            m = i;
        }

        m = m%n;
        println!("m={}",m)
    }

    n
}


fn main() {
    println!("Value = {}", gcd(20,23));
}
