
fn get_common_string<'a> (x1: &'a str, y1: &'a str) -> &'a str
{
    
    let x = x1.as_bytes();
    let y = y1.as_bytes();
    let min_len = std::cmp::min(x.len(), y.len());

    for i in 0..min_len {
        if x[i] != y[i] {
            return &x1[..i];
        }
    }
    return &x1[..min_len];
}


fn main() {

    let s1 = "where";
    let s2 = "when";

    let result = get_common_string(&s1, &s2);

    println!("result = {:?}", result);
}




