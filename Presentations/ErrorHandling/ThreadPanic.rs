use std::thread;

fn main() {
    let a = 0;
    let b = 10;
    let handle = thread::spawn (
        move || {
            let c = b/a;
            //panic!("Under panic!!!");
        }
    );

    let result = handle.join();
    match result {
        Ok(_) => println!("Thread was succesfully exited!!!"),
        Err(e) => println!("There is problem in thread. Erro: {:?}", e),
    }
}


