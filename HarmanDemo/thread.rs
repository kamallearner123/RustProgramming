use std::sync::{Arc, Mutex};
use std::thread;
fn main() {
    //global_data is protected with Arc and syn with Mutex
    let global_data = Arc::new(Mutex::new(vec![]));
    let handles = vec![];

    for i in 0..10 {
        //Creating another variable/pointer pointing to same data//
        let thread_data = Arc::clone(&global_data);
        let handle = thread(move || {
            //Get lock
            let local = thread_data.lock();
            thread_data.push(i);
        });

        handles.push(handle);
    }

    for handle in handles {
        handle.join();
    }

    for i in global_data {
        println!(" i = {}", i);
    }


}