fn main() {

    let mut v1: Vec<i32> = vec![1,2,3,4,];
    let target = 100;

    let a = loop {
        if let Some(p) = v1.pop() {
            if p == target {
                break "Got it";
            }
        }else {
            break "Not found";
        }
    };
 
    println!("a = {}", a);
    println!("{:?}",v1);
}