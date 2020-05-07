# Time Cost: O(n)
# Space Cost: O(n)

def climb_stairs(n):
    if n == 1:
        return 1

    paths = [0] * n
    paths[0], paths[1] = 1, 2

    for i in range(2, n):
        paths[i] = paths[i-1] + paths[i-2]

    return paths[n-1]
