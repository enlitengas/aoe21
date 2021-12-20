use std::io::{BufRead, BufReader};
use std::fs::File;


fn main() {
    // --snip--
    let filename = "input.txt";
    println!("In file {}", filename);
    // Open the file in read-only mode (ignoring errors).
    let file = File::open(filename).unwrap();
    let reader = BufReader::new(file);

    let mut count: i32 = 0;
    let mut array: [i32; 4] = [0; 4];
    let mut offset = 0;
    // Read the file line by line using the lines() iterator from std::io::BufRead.
    for (index, line) in reader.lines().enumerate() {
        offset = index % 4;
        if index > 3 {
            let sum1 = array[offset % 4]+array[(1+offset)%4]+array[(offset+2)%4];
            let sum2 = array[(1+offset)%4]+array[(offset+2)%4]+array[(offset+3)%4];
            if sum2 > sum1 {
                count+=1;
            } 
        }

        let line = line.unwrap(); // Ignore errors.
        // Show the line and its number.
        let depth = line.parse::<i32>().unwrap();
        array[index % 4] = depth;
    }
    offset = (offset + 1) % 4;
    let sum1 = array[offset % 4]+array[(1+offset)%4]+array[(offset+2)%4];
    let sum2 = array[(1+offset)%4]+array[(offset+2)%4]+array[(offset+3)%4];
    if sum2 > sum1 {
        count+=1;
    }
    println!("Count: {}.", count);
}
