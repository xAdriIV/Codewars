def row_sum_odd_numbers(n):
    sum = 0
    start = (n * n) - (n - 1)
    end = start + n * 2
    for i in range(start, end, 2):
        sum += i
    return sum