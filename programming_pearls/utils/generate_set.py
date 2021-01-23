import sys
from random import sample


def generate_ints(max_num, num_elements):
    ints = sample(range(max_num), k=num_elements)

    with open("integer_set.txt", "w+") as f:
        for i in ints:
            f.write(str(i))
            f.write("\n")



if __name__ == "__main__":
    n, k = sys.argv[1:]
    generate_ints(int(n), int(k))
