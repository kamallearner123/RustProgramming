#[derive(Debug)]
struct Student {
    name:String,
    roll:i32
}

fn main() {
    let s1:Student = Student{name:String::from("Kamal"),
                            roll:32};
    println!("details = {:?}", s1);
}
