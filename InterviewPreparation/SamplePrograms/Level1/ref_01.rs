
fn add(a:i32,b:i32) -> i32
{
    return a+b;
}
fn main() {
    let wish:String = String::from("Hello");
    let ref_wish = &wish;
    
    println!("wish = {}, {}", wish, ref_wish);
    println!("wish = {}", wish);
    
    
    let a:i32 = 10;
    let b:i32 = 20;
    let result = add(a,b);
    println!("resul = {}", result);
    println!("a+b = {}", a+b);
    println!("a = {}, b = {}", a,b);
}
