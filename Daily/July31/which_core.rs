use libc::sched_getcpu;

fn main() {
    unsafe {
        let cpu = sched_getcpu();
        if cpu >= 0 {
            println!("Running on CPU/Core: {}", cpu);
        } else {
            eprintln!("Failed to get CPU/core ID.");
        }
    }
}

