pub fn add(i:i32, j:i32) -> i32 {
    i + j
}   

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_it_works() {
        let result = add(2, 2);
        assert_eq!(result, 4);
    }
}
