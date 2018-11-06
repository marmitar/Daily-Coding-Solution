use std::collections::VecDeque;

fn calc_lvl(file: &str) -> usize {
    let mut level = 0;

    for ch in file.chars() {
        level += 1;
        if ch != '\t' {
            break;
        }
    }

    return level;
}

fn pathgen(dirs: &VecDeque<String>) -> String {
    let mut path = "".to_string();

    for dir in dirs.iter().rev() {
        path.push_str(dir);
        path.push('/');
    }
    path.pop();

    return path;
}

fn longest_path(filesys: &str) -> String {
    let mut dirpath = VecDeque::<String>::new();

    let mut max_path = "".to_string();
    let mut last_lvl = 0;

    for file in filesys.lines() {
        let level = calc_lvl(file);
        let filename = file.trim_left_matches('\t').to_string();
        let is_file = filename.contains('.');

        while last_lvl >= level {
            dirpath.pop_front();
            last_lvl -= 1;
        }

        dirpath.push_front(filename);
        last_lvl += 1;

        let path = pathgen(&dirpath);
        if is_file && path.len() > max_path.len() {
            max_path = path;
        }
    }

    return max_path;
}

fn main() {
    let input = vec![
        "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext",
        "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    ];

    for fs in input {
        let max = longest_path(&fs);
        println!("{}: {}", max.len(), max);
    }
}
