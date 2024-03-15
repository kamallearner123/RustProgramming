use std::io;

fn main() {
    let int1 = 10;
    let int2 = int1;

    println!("int1 = {}, int2 = {}", int1, int2);

    let mut data1 = String::new();
    let mut data2 = String::new();

    let _result1 = io::stdin().read_line(&mut data1);
    let _result2 = io::stdin().read_line(&mut data2);


    owner_fun(data1);
    //println!("data1 = {}", data1);

    borrow_fun(&data2);
    println!("data2 = {}", data2);
}

fn owner_fun(data: String) {
    println!("data = {}", data);
}

fn borrow_fun(data:& String) {
    println!("data = {:#?}", data);
}

