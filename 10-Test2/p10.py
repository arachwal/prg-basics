def f(array):
    min_value = float('inf')  # start with infinity
    min_row = -1
    min_col = -1

    for i, row in enumerate(array):
        for j, value in enumerate(row):
            if value < min_value:
                min_value = value
                min_row = i
                min_col = j

    # Check if row index == column index
    return min_row == min_col

array=([[7,8],[5,3],[9,4]])
print(f(array))

