enum Direction {
	Up,
	Down,
	Right,
	Left,
	Wrong,
}

fn my_fun(num: i32) -> Direction {
	match num {
		0..=10 => return Direction::Up,
		11..=20=> return Direction::Down,
		21..=30 => return Direction::Left,
		31..=40 => return Direction::Right,
		_=> return Direction::Wrong,
	}
}


fn main() {
	match my_fun(10) {
		Direction::Up => println!("Moving up!!!"),
		Direction::Down => println!("Moving down!!!"),
		_=> println!("Default"),
	}
}
