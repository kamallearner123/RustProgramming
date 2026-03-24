use std::rc::Rc;
use std::cell::RefCell;

fn main() {

    let mut rCount = Rc::new(RefCell::new(String::from("Hello")));
    println!("{}",rCount.borrow());

    let r1 = rCount.clone();
    r1.borrow_mut().push_str(" world!!!");

    rCount.borrow_mut().push_str(" world!!!");
    println!("{}",rCount.borrow());
    println!("{}",r1.borrow());

}
