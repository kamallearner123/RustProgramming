use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
	let data = Arc::new(Mutex::new(5));
	println!("Value = {}", *data.lock().unwrap());
}
