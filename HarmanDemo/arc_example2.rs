use std::sync::{Arc,Mutex};
use std::thread;

fn main() {
	
	let data = Arc::new(Mutex::new(vec![]));
	
	let mut handles = vec![];

	for i in 1..5 {
		let data = Arc::clone(&data);	
		let handle = thread::spawn(move|| {
			let mut my_data = data.lock().unwrap();
			my_data.push(i);
			println!("Thread");
		}
		);
		handles.push(handle);
	}

	for handle in handles {
		handle.join().unwrap();
	}
}
