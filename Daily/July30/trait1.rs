

trait Printable {
    fn print_data(&self);
}

struct Message {
    id: u8,
    message: String
}


impl Printable for Message {
    fn print_data(&self) {
        println!("Data -> Message ID:{}, Message:{}", self.id, self.message);
    }
}



fn compare(s1:String, s2:String) -> bool {
    if s1==s2 {
        return true;
    } else {
        return false;
    }
}
fn main() {
    let m1: Message = Message{id:10, message:String::from("Hello")};
    m1.print_data();
    
    let s1 = String::from("Kamal");
    let s2 = String::from("Kumar");
    println!("Result = {}", compare(s1.clone(),s2));

    println!("s1 = {}", s1);

}
