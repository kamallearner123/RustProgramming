use std::sync::Mutex;
use lazy_static::lazy_static;


/// Define a mutable global variable///
lazy_static! {
    static ref GLOBAL_COUNTER: Mutex<i32> = Mutex::new(100);
    static ref GLOBAL_COUNTER2: Mutex<i32> = Mutex::new(100);
}


fn fun1() {
    let mut counter = GLOBAL_COUNTER.lock().unwrap();
    *counter = *counter + 1;
}

fn fun2() {
    let mut counter = GLOBAL_COUNTER.lock().unwrap();
    *counter = *counter + 1;
}


fn main() {
    fun1();
    fun2();
    let counter = GLOBAL_COUNTER.lock().unwrap();
    println!("{}", counter);
}


// write the test code for the above functions
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_fun1() {
        fun1();
        let counter = GLOBAL_COUNTER.lock().unwrap();
        assert_eq!(*counter, 101);
    }

    #[test]
    fn test_fun2() {
        fun2();
        let counter = GLOBAL_COUNTER.lock().unwrap();
        assert_eq!(*counter, 102);
    }
}
// explaina about Rc and Arc in Rust
// Rc: Rc is a reference-counted smart pointer in Rust. 
// It is used to allocate memory on the heap and share it between multiple owners. Rc stands for Reference Counted. It keeps track of the number of references to a value and deallocates the memory when the number of references drops to zero. Rc is used when you want to share ownership of a value between multiple owners. Rc is not thread-safe and cannot be used in multi-threaded programs. Rc is used when you want to share ownership of a value between multiple owners. Rc is not thread-safe and cannot be used in multi-threaded programs.
// Arc: Arc is an atomic reference-counted smart pointer in Rust. It is used to allocate memory on the heap and share it between multiple owners. Arc stands for Atomic Reference Counted. It keeps track of the number of references to a value and deallocates the memory when the number of references drops to zero. Arc is used when you want to share ownership of a value between multiple owners in a multi-threaded program. Arc is thread-safe and can be used in multi-threaded programs. Arc is used when you want to share ownership of a value between multiple owners in a multi-threaded program. Arc is thread-safe and can be used in multi-threaded programs.
