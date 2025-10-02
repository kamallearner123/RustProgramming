use std::rc::Rc;
use std::cell::RefCell;

fn main() {

    let mut rCount = Rc::new(RefCell::new(String::from("Hello")));
    println!("{}",rCount.borrow());

    rCount.borrow_mut().push_str(" world!!!");
    println!("{}",rCount.borrow());

}
