from collections import deque


def count_lvl(file):
    level = 0

    for char in file:
        level += 1
        if char != '\t':
            break
    return level


def pathgen(dirs):
    return '/'.join(dirs)


def longest_path(filesystem):
    last_level = 0
    max_path = ""

    dirpath = deque()

    for file in filesystem.splitlines():
        lvl = count_lvl(file)
        filename = file.lstrip('\t')

        if lvl <= last_level:
            path = pathgen(dirpath)
            if len(path) > len(max_path):
                max_path = path

            while last_level >= lvl:
                dirpath.pop()
                last_level -= 1

        dirpath.append(filename)
        last_level += 1

    path = pathgen(dirpath)
    if len(path) > len(max_path):
        max_path = path

    return max_path


if __name__ == "__main__":
    paths = [
        "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext",
        "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    ]

    for path in paths:
        print(longest_path(path))