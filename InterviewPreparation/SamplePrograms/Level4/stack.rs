use std::fmt::Debug;

trait Printable {
    fn print_data(&self);
}


#[derive(Debug)]
struct Stack<T> {
    items:Vec<T>,
}


impl<T:Debug> Printable for Stack<T> {
    fn print_data(&self) {
        for i in &self.items {
            println!("Data : {:?}", i);
        }
    }
}

impl Stack<T> {
    fn new() -> Self {
        Stack{items:Vec::new()}
    }
    fn push(&mut self, data:T) {
        self.items.push(data);
    }
}

fn main() {
    
    let mut mystack:Stack<i32> = Stack::new();

    mystack.push(100);
    mystack.push(100);
    mystack.push(100);
    mystack.push(100);
    mystack.push(100);

    mystack.print_data();
}

