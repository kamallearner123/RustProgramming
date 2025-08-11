use std::thread;
use std::time::Duration;
fn main() {
    let handle = thread::spawn(||
        {
            for i in 0..10 {
                println!("i={}", i);
                thread::sleep(Duration::from_millis(1000));
            }
        }
    );

    let _ = handle.join();
}
