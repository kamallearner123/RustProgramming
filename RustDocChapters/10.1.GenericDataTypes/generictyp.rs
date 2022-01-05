#[derive(Debug)]
struct Point<T> {
    x:T,
    y:T,
}

impl <T> Point<T> {

    fn print_data(&self) {
        println!("Point x ={}, y= {}", &self.x, &self.y);
    }
    
}

fn main() {

    let p1 = Point{y:1,x:2};

    p1.print_data();

}
