use std::io::{BufRead, BufReader};
use std::fs::File;


fn main() {
    // --snip--
    let filename = "input.txt";
    println!("In file {}", filename);
    // Open the file in read-only mode (ignoring errors).
    let file = File::open(filename).unwrap();
    let reader = BufReader::new(file);

    let mut depth = 0;
    let mut hori = 0;
    let mut aim = 0;
    // Read the file line by line using the lines() iterator from std::io::BufRead.
    for (index, line) in reader.lines().enumerate() {
        let line = line.unwrap();
        let mut params = line.split(' ');
        let cmd = params.next().unwrap();
        let num = params.next().unwrap().parse::<i32>().unwrap();
        match cmd {
            // The arms of a match must cover all the possible values
            "forward" => {
                hori += num;
                depth += aim*num;
            },
            "down" => aim += num,
            "up" => aim -= num,
            _ => println!("Error")
            // TODO ^ Try commenting out one of these arms
        };
    }

    println!("Depth: {}. Horizontal: {}. Product: {}.", depth, hori, depth*hori);
}
