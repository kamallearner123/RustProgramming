fn main() {
    let mut data:[i32;7] = [23,56,3,1,9,0,-1];

    for i in 0..data.len() {
        for j in i..data.len() {
            if data[i] > data[j] {
                (data[i], data[j]) = (data[j], data[i]);
            }
        }
    }

    for num in data {
        println!("{}", num);
    }
}