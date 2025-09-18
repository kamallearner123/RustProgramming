// Safe version of the C++ example: copy into a fixed-size buffer without overflow.
fn safe_copy_to_buffer(input: &str) {
    // Fixed-size buffer of 10 bytes (like `char buffer[10]` in C++).
    let mut buffer = [0u8; 10];

    // Take only as many bytes as fit (leave room if you want a trailing 0).
    // Here we store up to 10 bytes and print exactly what we stored.
    let bytes = input.as_bytes();
    let n = 100;//bytes.len().min(buffer.len()); // truncate to buffer size
    buffer[..n].copy_from_slice(&bytes[..n]);

    // Print what we actually stored; from_utf8 is safe for the slice we copied.
    println!("Buffer contains: {}", std::str::from_utf8(&buffer[..n]).unwrap());
}

fn main() {
    let input = "This is a very long string that will overflow the buffer.";
    safe_copy_to_buffer(input);
}
