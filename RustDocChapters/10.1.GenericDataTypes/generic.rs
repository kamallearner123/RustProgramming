fn largets(list: &[i32]) -> &i32 {

    let mut largest:&i32 = &list[0];

    for i in list {
        println!("i = {}", i);
        if i>largest {
            largest = i;
        }
    }

    largest
}

fn main() {
    let number_list = vec![34, 50, 25, 100, -10, 65];

    println!("The largest number is {}", largets(&number_list));
}

