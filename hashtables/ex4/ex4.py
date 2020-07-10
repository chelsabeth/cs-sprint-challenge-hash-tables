def has_negatives(a):
    result = []
    cache = {}

    for num in a:
        # make sure 0 isn't saved, skip over it if it's there
        if num == 0:
            continue

        # calculate inverse
        inverse = (num - (num * 2))

        # check and see if the inverse of the num is already in the cache
        # if it is append it to the results list
        if inverse in cache:
            if num < 0:
                result.append(inverse)
            else:
                result.append(num)

        # if not save the current num/inverse pair and keep on going
        cache[num] = inverse

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

    a = list(range(5000000))
    a += [-1,-2,-3]

    result = has_negatives(a)
    result.sort()
    print(result)
