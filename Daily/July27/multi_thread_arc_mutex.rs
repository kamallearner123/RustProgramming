use std::thread;
use std::sync::{Arc, Mutex};
fn main() {
    let mut handles = vec![];

    let ref_count:Arc<Mutex<i32>> = Arc::new(Mutex::new(0));

    for i in 1..=10 {
        let local = ref_count.clone();
        handles.push(thread::spawn(
            move || {
                println!("item in thread = {:?}", i);
                let mut data = local.lock().unwrap();
                *data += 1;
            }
        ));
    }
    

    for handle in handles {
        println!("Return value of join = {:?}", handle.join());
    }


    let val = ref_count.lock().unwrap();
    println!("ref_count = {}", *val);
}
