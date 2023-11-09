    arr.sort()  # Sort the array in non-decreasing order
    result = []  # Result array to store the number of sticks before each iteration

    while arr:
        result.append(len(arr))  # Append the length of the current array
        shortest_stick = arr[0]  # Length of the shortest stick

        # Subtract the length of the shortest stick from each element
        arr = [stick - shortest_stick for stick in arr]

        # Remove any sticks with zero or negative length
        arr = [stick for stick in arr if stick > 0]

    return result
