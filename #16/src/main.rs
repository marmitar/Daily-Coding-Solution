struct Log {
    mem: Vec<u64>,
    cap: usize,
    pos: usize
}

impl Log {
    fn record(&mut self, order_id: u64) {
        self.mem[self.pos] = order_id;
        self.pos = (self.pos + 1) % self.cap;
    }

    fn get_last(&self, i: usize) -> u64 {
        let p = (self.cap + self.pos - i) % self.cap;
        return self.mem[p];
    }
}

fn init(size: usize) -> Log {
    let mut log = Log {
        mem: Vec::<u64>::with_capacity(size),
        cap: size,
        pos: 0
    };

    for _ in 0..size {
        log.mem.push(0);
    }

    return log;
}

fn main() {
    let mut log = init(10);
    log.record(111);
    log.record(222);

    for val in &log.mem {
        print!("{} ", val);
    }
    println!("");

    println!("{}", log.get_last(2));
}
