filename = 'wcfile.txt'

num_lines = 0
num_words = []
num_chars = 0


with open(filename) as f:
    for line in f:
        num_lines += 1
        num_chars += len(line)

        if not line.startswith('\n'):
            num_words.extend(line.rstrip().split(' '))

print(f'Number of lines: {num_lines}')
print(f'Number of words: {len(num_words)}')
print(f'Number of unique words: {len(set(num_words))}')
print(f'Number of chars: {num_chars}')
