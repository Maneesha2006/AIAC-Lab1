def factr_corrected(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factr_corrected(n - 1)

print(factr_corrected(5))
