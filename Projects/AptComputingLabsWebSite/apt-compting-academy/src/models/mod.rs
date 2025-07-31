// This file defines the data models used in the application. 
// It includes structures and methods for handling data.

pub struct Course {
    pub id: u32,
    pub name: String,
    pub description: String,
}

impl Course {
    pub fn new(id: u32, name: String, description: String) -> Self {
        Course { id, name, description }
    }
}

pub struct Student {
    pub id: u32,
    pub name: String,
    pub email: String,
}

impl Student {
    pub fn new(id: u32, name: String, email: String) -> Self {
        Student { id, name, email }
    }
}