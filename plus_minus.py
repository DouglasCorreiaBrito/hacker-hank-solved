def plusMinus(arr):
    result_list = []
    length = len(arr)
    positives_values = 0
    negatives_values = 0
    zero_values = 0
    for element in arr:
        if element > 0:
            positives_values += 1
        if element < 0:
            negatives_values += 1
        if element == 0:
            zero_values += 1
    result_list.extend([positives_values, negatives_values, zero_values])
    final_list = [value/length for value in result_list]
    for i in final_list:
        print("{:.6f}".format(i));
