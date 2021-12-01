fn reverse(pair: (u32, bool)) -> (bool, u32) {

    let (integet, boolean) = pair; //Same as python
    (boolean, integet)
}


fn main() {
 
    let (t1, _) = reverse((100, true));
    println!("t1 = {}", t1);
}
