from collections import deque


def max_k_length_subarrays(array, k):
    queue = deque(array[:k])

    rp = 0
    lp = k - 1

    while (rp < len(array)-k):
        array[rp] = max(queue)
        queue.append(array[k+rp])
        queue.popleft()
        rp += 1

    array[rp] = max(queue)

    return array[:rp+1]
