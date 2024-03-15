use std::io;

fn main() {
    let mut my_data = String::from("apt sfotware solutions");
    println!("{:?}", my_data);

    println!("{}", len_string(&my_data));

    change_data(&mut my_data);
    println!("{:?}", my_data);

}

fn len_string(data: &String) -> usize {
    data.len()
}

fn change_data(data:&mut String) {
    data.push_str("____");
}
