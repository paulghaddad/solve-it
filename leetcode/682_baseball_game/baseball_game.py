from stack import Stack

# Time Complexity: O(n)
# Space Complexity: O(n)

def cal_points(ops):
    stack = Stack()

    for op in ops:
        try:
            stack.push(int(op))
        except ValueError as e:
            if op == 'C':
                stack.pop()
            elif op == 'D':
                previous_valid_score = stack.peek()
                stack.push(2 * previous_valid_score)
            elif op == '+':
                previous_two_round_scores = [stack.pop(), stack.pop()]
                current_round_score = sum(previous_two_round_scores)
                stack.push(previous_two_round_scores.pop())
                stack.push(previous_two_round_scores.pop())
                stack.push(current_round_score)
            else:
                raise ValueError(f'An invalid argument was provided: {op}')

    point_total = 0
    while not stack.is_empty():
        point_total += stack.pop()

    return point_total
