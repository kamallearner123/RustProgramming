use recuerdame::precalculate;

#[precalculate(a=0..=10, b=0..=4)]
pub const fn add(a:i32, b:i32) -> i32 {
    a+b
}


fn main() {
    let result = add(1,2);
    println!(" 1+2 = {result}");
}
