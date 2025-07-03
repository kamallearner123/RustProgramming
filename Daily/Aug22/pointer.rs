fn main() {
    let x = 10;
    let p = &x;

    println!("{},{}, {}", x, *p, p);
}
