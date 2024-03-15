
struct Server {
    address:String,
}

impl Server {
    fn new(s:String) -> Self {
        Self {
            address:s
        }
    }
}
fn main() {
    let ipdetails = String::from("192.168.0.0.1:8080");
    let _server = Server::new(ipdetails);
    println!("Hello, world!");
}

// Code to be tested
fn add(a: i32, b: i32) -> i32 {
    a + b
}

// Test module
#[cfg(test)]
mod tests {
    // Import the `add` function from the outer module
    use super::*;

    // Test function
    #[test]
    fn test_add() {
        // Arrange: Set up the test inputs
        let x = 3;
        let y = 5;

        // Act: Call the function being tested
        let result = add(x, y);

        // Assert: Check the result
        assert_eq!(result, 8);
    }
}




