from glob import glob

def get_filenames(directory):
    return glob(directory + '/*.txt')


def get_longest_word(filename):
    longest_word = ''

    with open(filename) as f:
        for line in f:
            longest_word_of_line = max(line.strip().split(' '), key=len)
            if len(longest_word_of_line) > len(longest_word):
                longest_word = longest_word_of_line

        return longest_word

if __name__ == '__main__':
    directory = 'sample_books'
    files = get_filenames(directory)

    longest_words_per_file = {
        filename: get_longest_word(filename)
        for filename in files
    }

    print(longest_words_per_file)
