extern crate ndarray;
use ndarray::Array2;

pub fn minimum_cost(costs: &Array2<f64>) -> f64 {
    let mut sum = 0.0;
    for cost in costs.iter() {
        sum += cost;
    }
    return sum;
}