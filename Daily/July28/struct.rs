

#[derive(Debug)]
struct Student {
    name:String,
    age:i32
}

fn main() {
    let s1:Student = Student{name:String::from("Kamal"),
                        age:30};
    println!("DAta = {:?}", s1);
}

