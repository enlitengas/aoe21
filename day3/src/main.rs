use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    // --snip--
    let filename = "test.txt";
    const l: usize = 5;
    println!("In file {}", filename);
    // Open the file in read-only mode (ignoring errors).
    let mut file = File::open(filename).unwrap();
    let mut reader = BufReader::new(file);

    let mut gamma = 0;
    let mut elips = 0;
    let mut lines: u32 = 0;
    let mut array: [u32; l] = [0; l];
    // Read the file line by line using the lines() iterator from std::io::BufRead.
    for (_index, line) in reader.lines().enumerate() {
        let line = line.unwrap();
        for (i,c) in line.chars().enumerate() {
            array[i] += c.to_digit(2).unwrap();
        }
        lines += 1;
    }
    println!("{}", lines);
    lines /= 2;
    let mut co2: String = "".to_owned();
    let mut oxy: String = "".to_owned();
    for (i,n) in array.iter().enumerate() {
        let bit = (n > &lines) as u32;
        let p = (2 as i32).pow(i as u32);
        match bit {
            1 => {
                gamma += p;
                oxy.push_str("1");
                co2.push_str("0");
            },
            0 => {
                elips += p;
                oxy.push_str("0");
                co2.push_str("1");
            },
            _ => println!("ERROR")
        }
        
    }
    println!("gamma: {}. elipson: {}. product: {}", gamma, elips, gamma*elips);
    let mut best_oxy: &str;
    let mut oc = 0;
    let mut best_co2: &str;
    let mut cc = 0;

    let mut oxy_chars = oxy.chars();

    file = File::open(filename).unwrap();
    reader = BufReader::new(file);
    for (_index, line) in reader.lines().enumerate() {
        let line = line.unwrap();
        print!("{}. ", line);

        let mut score = 0;
        for (i,c) in line.clone().chars().enumerate() {
            if c == oxy_chars.next().unwrap() {
                score += 1;
            } else {
                break;
            }
        }
        if score > oc {
            println!("BEST!");
           // best_oxy = &linecopy;
        } else {
            println!("");
        }
    }
   // println!("best oxy: {}", best_oxy);
    println!("oxy: {}. co2: {}.", oxy, co2);
    //println!("{}{}{}{}{}", array[0] > lines,array[1],array[2],array[3],array[4]);
}
