
pub mod pixel_mod {
    pub use std::fmt::{self, Debug};

    pub struct GrayscaleMap {
        pub pixels_data : Vec<u8>,
        pub size: (usize, usize)
    }

    impl GrayscaleMap {
        pub fn new(rows: usize, cols: usize) -> GrayscaleMap {
            GrayscaleMap {
                pixels_data: vec![0; rows*cols],
                size: (rows, cols)
            }
        }
    }

    impl Debug for GrayscaleMap {
        fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
            write!(f, "GrayscaleMap {:?} {:?}", self.size, self.pixels_data)
        }
    }

    impl Clone for GrayscaleMap {
        fn clone(&self) -> GrayscaleMap {
            GrayscaleMap {
                pixels_data: self.pixels_data.clone(),
                size: self.size
            }
        }
    }


    impl PartialEq for GrayscaleMap {
        fn eq(&self, other: &GrayscaleMap) -> bool {
            self.pixels_data == other.pixels_data && self.size == other.size
        }
    }

}