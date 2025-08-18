extern "C" {
    fn strlen(s:*const u8)->usize;
}

fn main() {
    let mut num = 5;
    let r1 = &num as *const i32;
    let r2 = &mut num as *mut i32;


    unsafe {
        println!("r1 : {}", *r1);
        *r2 = *r2+10;
        println!("r2 = {}", *r2);
    }


    let wish = "Hello world";
    let ptr = wish.as_ptr();
    let len = unsafe {strlen(ptr)};
    println!("Length = {}", len);
}
