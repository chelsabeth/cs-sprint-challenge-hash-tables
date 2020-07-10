class Entry:
    def __init__(self, weight, count):
        self.weight = weight
        self.next = None
        self.count = count


def get_indices_of_item_weights(weights, length, limit):
    # Cache to store the entries
    cache = {}
    # tracker to keep track of the index
    count = 0 

    # get each weight out of the weights list
    for weight in weights:
        # make a new entry
        entry = Entry(weight, count)
        # see if the weight already exists in the cache
        if weight in cache:
            # if it does, then add a new node to the LinkedList
            cache[weight].next = entry

            # if these two numbers combined equal the desired weight limit return 
            # them in the correct order
            if limit == weight + weight:
                return cache[weight].next.count, cache[weight].count

            
        # add the new entry to the cache 
        cache[weight] = entry

        # calculate missing number if the using the most recently added weight to make up the limit
        neededWeight = limit - weight 

        # if the other missing number already exists then great, go ahead and 
        # return them - make sure it doesnt do this if its multiples of the same number
        if (neededWeight in cache) and (neededWeight != weight):
            if cache[weight].count > cache[neededWeight].count:
                return cache[weight].count, cache[neededWeight].count
            else:
                return cache[neededWeight].count, cache[weight].count

        # increments index and loop through again
        count += 1

    # if there are no two numbers that make up the limit then return None
    return None


if __name__ == "__main__":
    weights_1 = [9]
    weights_2 = [4, 4]
    weights_3 = [4, 6, 10, 15, 16]
    weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
    print(get_indices_of_item_weights(weights_1, 1, 9))
    print(get_indices_of_item_weights(weights_2, 2, 8))
    print(get_indices_of_item_weights(weights_3, 5, 21))
    print(get_indices_of_item_weights(weights_4, 9, 7))
