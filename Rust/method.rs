struct Char {
    hp: i32,
    mp: i32,
    attk: i32,
}

impl Char {
    fn get_attk(&self) -> i32 {
        self.attk
    }
    fn get_hp(&self) -> i32 {
        self.hp
    }
    fn get_mp(&self) -> i32 {
        self.mp
    }
}

impl Drop for Char {
    fn drop(&mut self) {
        println!("drop");
    }
}

fn main() {
    let a = Char { hp: 100, mp: 50, attk: 10};
    println!("{}, {}, {}", a.get_hp(), a.get_mp(), a.get_attk());
}
