def get_last_line(filename):
    with open(filename) as f:
        lines = f.readlines()
        return lines[-1]

print(get_last_line('test.txt'), end='')
