fn calc_pi(points: u64) -> f64 {
    let mut inside = 0;
    let radius = 1.0;
    let rad_sq = radius * radius;
    let square_area = 1.0 * 1.0;

    for _ in 0..points {
        let x: f64 = rand::random();
        let y: f64 = rand::random();

        if x*x + y*y <= rad_sq {
            inside += 1;
        }
    }

    let upper: f64 = 4.0 * (inside as f64) * square_area;
    let lower: f64 = (points as f64) * square_area;
    let pi = upper/lower;
    return pi;
}


fn main() {
    for arg in std::env::args().skip(1) {
        let points: u64 = arg.parse().unwrap();
        let pi = calc_pi(points);

        println!("With {} points, we got `pi` ~= {}", points, pi);
    }
}
