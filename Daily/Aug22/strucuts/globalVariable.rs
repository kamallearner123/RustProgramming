extern crate lazy_static;
use std::sync::Mutex;
use lazy_static::lazy_static;

/// Define a mutable global variable///
lazy_static! {
    static ref GLOBAL_COUNTER: Mutex<i32> = Mutex::new(100);
    static ref GLOBAL_COUNTER2: Mutex<i32> = Mutex::new(100);
}


fn fun1() {
    let counter = GLOBAL_COUNTER.lock().unwrap();
    counter +=1;
}

fn fun2() {
    let counter = GLOBAL_COUNTER.lock().unwrap();
    counter +=1;
}


fn main() {
    fun1();
    fun2();
    let counter = GLOBAL_COUNTER.lock().unwrap();
    println!("{}", counter);
}


