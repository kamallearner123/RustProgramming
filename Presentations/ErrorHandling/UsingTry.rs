
// enum MyResult <T, E> {
//     Okk(T),
//     NotOk(E),
// }

// fn dummy_dev(i:i32, j:i32) -> MyResult<i32, String> {
//     if j==0 {
//         MyResult::NotOk("Error: devide by 0".to_string())
//     } else {
//         MyResult::Okk(i/j)
//     }
// }
// fn main() {

//     match dummy_dev(1, 2) {
//         MyResult::Okk(data) => println!("Value : {}", data),
//         MyResult::NotOk(error) => println!("Error: {}", error),
//     }

// }

// enum Result<T, E> { 
//     Ok(T), 
//     Err(E), 
// }

fn divide(a: f64, b: f64) -> Result<f64, String> {
    if b == 0.0 {
        Err(String::from("Division by zero"))
    } else {
        Ok(a / b)
    }
}

fn main() {
    match divide(4.0, 2.0) {
        Ok(result) => println!("Result: {}", result.unwrap()),
        Err(e) => println!("Error: {}", e.expect("Issue")),
    }
}