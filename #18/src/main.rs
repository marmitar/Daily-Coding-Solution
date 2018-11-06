fn max(array: &[u64]) -> u64 {
    let mut max = u64::min_value();

    for value in array {
        if *value > max {
            max = *value;
        }
    }

    return max;
}

fn subars_maxs(array: &Vec<u64>, k: usize) -> Vec<u64> {
    let mut maxs: Vec<u64> = Vec::new();

    for i in 0..array.len()-(k-1) {
        let submax = max(&array[i..i+k]);
        maxs.push(submax);
    }

    return maxs;
}

fn main() {
    let array = vec![10, 5, 2, 7, 8, 7];

    for max in subars_maxs(&array, 3) {
        println!("{}", max);
    }
}
