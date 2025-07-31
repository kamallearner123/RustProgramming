fn main()
{
    let s1 = "hello world, hello rust";
    let sub = "rust";

    println!("Count = {}", s1.matches(sub).count());

    let ref_str = &s1[..5];
    println!("ref_str = {}", ref_str);
}
