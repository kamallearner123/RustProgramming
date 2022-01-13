struct Person {
    name:String,
    id:i32
}


impl Person {
    fn print(self) {
        println!("Name = {}, Id = {}", self.name, self.id);
    }
}


fn main() {
    let kamal = Person {name: "Kamal".to_string(), id: 100};
    kamal.print();
}
