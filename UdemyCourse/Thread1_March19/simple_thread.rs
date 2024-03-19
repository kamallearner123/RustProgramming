use std::thread;

fn main() {
    let handle = thread::spawn(|| {
        println!("In thread!!!");
    });

    println!("In main thread!!!");

    handle.join().expect("Thread panicked");
}
