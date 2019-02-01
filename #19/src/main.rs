extern crate ndarray;
extern crate rand;
mod builder;

use ndarray::Array2;
use builder::minimum_cost;

fn array_gen(m: usize, n: usize) -> Array2<f64> {
    let mut array = Array2::<f64>::zeros((m, n));

    let max: f64 = 1000000.0;
    for i in 0..m {
        for j in 0..n {
            array[[i, j]] = max * rand::random::<f64>() * rand::random::<f64>();
        }
    }

    return array;
}

pub fn main() {
    let arr = array_gen(2, 2);
    let cost = minimum_cost(&arr);

    println!("{}", cost);
}
