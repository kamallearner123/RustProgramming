use std::thread;

fn main() {
    let mut handles = vec![];

    let mut data:Vec<i32> = vec![1,2,3];


    for &item in &data[..2] {
        handles.push(thread::spawn(
            move || {
                println!("item in thread = {}", item);
            }
        ));
        //println!("item = {}", item);
    }
    //item is mutable reference &muti32
    /*
    for item in &mut data[..2] {
        *item = 0;
    }
    for item in &data[..2] {
        println!("... {}", *item);
    }
    for item in &data[..2] {
        // println! automatically dereferences item using Display trait.
        println!("... {}", item);
    }

    println!("Data in data = {:?}", data);

*/
    for item in data {
        println!("... {}", item);
    }
    for handle in handles {
        println!("Return value of join = {:?}", handle.join());
    }
}
