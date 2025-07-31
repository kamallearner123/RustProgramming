enum wendingState {
    Ordered,
    Processing,
    Dispatched,
    Exiting(i32)
}

fn main() {
    let mut option: wendingState = wendingState::Ordered;

    loop {
        match option {
            
            wendingState::Ordered => {println!("Ordered..");
                option = wendingState::Processing;
            },
            wendingState::Processing => {
                println!("Processing...");
                option = wendingState::Dispatched;
            },

            wendingState::Dispatched => {
                println!("Dispatched...");
                option = wendingState::Exiting(100);
            },
            wendingState::Exiting(val) => {
                println!("Existing.. with error code {}", val);
                break;
            }
            
        }
        
    }
}
