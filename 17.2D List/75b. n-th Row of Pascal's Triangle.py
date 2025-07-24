def get_row(n):
    row = [1]
    for k in range(1, n + 1):
        # Use formula: C(n, k) = C(n, k-1) * (n - k + 1) // k
        row.append(row[-1] * (n - k + 1) // k)
    return row

print(get_row(4))   # 4-th index ie 5th row
print(get_row(5))