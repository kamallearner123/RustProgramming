
// create a glbal variable to store the value of the counter
// use thread safe static mut to allow multiple threads to access the counter variable at the same time
// modify below code to modify COUNTER with thread safe apis and edit rest of the code accordingly
// static mut COUNTER: u32 = 0;

use std::sync::atomic::{AtomicU32, Ordering};

static COUNTER: AtomicU32 = AtomicU32::new(0);

fn increment() {
    COUNTER.fetch_add(1, Ordering::SeqCst);
}

fn main() {
    println!("Hello, world!");
    //create tow threads to increment the counter
    let handle = std::thread::spawn(|| {
        increment();
    });

    let handle2 = std::thread::spawn(|| {
        increment();
    });

    // wait for the threads to finish
    handle.join().unwrap();
    handle2.join().unwrap();

    // PRINT THE VALUE OF THE COUNTER
    println!("Counter: {}", COUNTER.load(Ordering::SeqCst));

}
