fn main() {
    let myv: Vec<i32> = [3,5,6,7].to_vec();
    for i in &myv {
        println!("{}", *i);
    }
}
