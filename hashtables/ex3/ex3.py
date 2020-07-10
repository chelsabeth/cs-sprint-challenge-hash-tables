def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    intersectNum = len(arrays)
    result = []

    # for every item in the arrays
    # see if there are duplicates of any one num
    # put that num in new array that will be the dup array
    for array in arrays:
        for num in array:
            if num in cache:
                cache[num] += 1
                if cache[num] == intersectNum:
                    result.append(num)
            else:
                cache[num] = 1

    return result



if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
