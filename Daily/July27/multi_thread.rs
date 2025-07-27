use std::thread;

fn main() {
    let mut handles = vec![];

    let mut data = vec![1,2,3];


    for &item in &data {
        handles.push(thread::spawn(
            move || {
                println!("Item = {}", item);
            }
        ));
    }
    for mut item in &data[..2] {
        *item = 0;
    }
    for &item in &data[..2] {
        println!("... {}", item);
    }
    for item in &data[..2] {
        println!("... {}", item);
    }

    println!("Data in data = {:?}", data);


/*    for item in data {
        println!("... {}", item);
    }*/

    for handle in handles {
        println!("Return value of join = {:?}", handle.join());
    }
}
