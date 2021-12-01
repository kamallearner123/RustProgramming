/*
#[...] is an attribute on struct Person. derive(Debug) asks the compiler 
to auto-generate a suitable implementation of the Debug trait, 
which provides the result of {:?} in something like 
format!("Would the real {:?} please stand up!", Person { name: "John", age: 8 });.
*/

#[derive(Debug)]
struct Person {
    name: String,
    age : u8,
}

#[derive(Debug)]
struct Student {
    name: String,
    age : u8,
    body :Person,
}

#[derive(Debug)]
struct Point (f32, f32);

fn main() {

    let name1 = String::from("Kamal");
    let age1 = 32;
    let name2 = String::from("Kamal");
    let age2 = 32;
    let kamal = Person{name:name1, age:age1};
    let dharshit = Student{name:name2, age:age2, body:kamal};

    println!("Details = {:?} \n", dharshit);


    // point (point)
    let point1 = Point(1.1,2.2);
    println!("{:?}", point1);
}
