


fn sample() -> Result<i32,std::io::Error> {
    Ok(0)
}

fn main() {
    println!("Hello, world!");
    let a = match sample {
        Ok(result) => result,
        Err(errno) => errno
    };

}
