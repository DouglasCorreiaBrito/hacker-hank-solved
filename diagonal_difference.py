def diagonalDifference(arr):
    # Write your code here
    lines = len(arr)
    main_diagonal = 0
    second_diagonal = 0
    last_value = lines - 1
    for i in range (0, lines):
        values = arr[i]
        main_diagonal += values[i]
        second_diagonal += values[last_value - i]
    return (abs(main_diagonal - second_diagonal))
