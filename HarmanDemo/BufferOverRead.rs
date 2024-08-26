fn main() {
    let arr = [1, 2, 3, 4, 5];

    // This loop will attempt to access an out-of-bounds index
    for i in 0..=5 {
        println!("Accessing index {}: {}", i, arr[i]);
    }
}

